package moa.classifiers.core.driftdetection;

import com.github.javacliparser.FloatOption;
import com.github.javacliparser.IntOption;
import com.google.common.collect.Lists;
import moa.core.ObjectRepository;
import moa.tasks.TaskMonitor;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 *  UM MÉTODO DE DETECÇÃO DE MUDANÇA BASEADO EM PSI.
 *
 *
 *  @author Luiz Eduardo Malanczyn de Oliveira, Gabriel Luiz Tokarski Soto
 *  @version $Revision: 1 $
 */
public class PSI extends AbstractChangeDetector {

    private static final long serialVersionUID = -3518369648142099719L;

    public IntOption minNumInstancesOption = new IntOption(
            "minNumInstances",
            'n',
            "The minimum number of instances before permitting detecting change.",
            30, 0, Integer.MAX_VALUE);

    public FloatOption warningLevelOption = new FloatOption(
            "warningLevel", 'w', "Warning Level.",
            2.0, 1.0, 4.0);

    public FloatOption outcontrolLevelOption = new FloatOption(
            "outcontrolLevel", 'o', "Outcontrol Level.",
            3.0, 1.0, 5.0);

    public IntOption tamanhoJanelaOption = new IntOption(
            "tamanhoJanela",
            't',
            "The minimum number of instances before permitting detecting change.",
            100, 0, Integer.MAX_VALUE);

    private int minNumInstances;

    private double warningLevel;

    private double outcontrolLevel;

    private int tamanhoJanela;

    private Double psi;

    public PSI() {
        resetLearning();
    }

    public ArrayList<Double> actualPrediction = new ArrayList<Double>();

    public ArrayList<Double> expectedPrediction = new ArrayList<Double>();

    @Override
    public void resetLearning() {
        psi = 0.0;
        minNumInstances = this.minNumInstancesOption.getValue();
        warningLevel = this.warningLevelOption.getValue();
        outcontrolLevel = this.outcontrolLevelOption.getValue();
        tamanhoJanela = this.tamanhoJanelaOption.getValue();
    }

    @Override
    public void input(double prediction) {
        // prediction must be 1 or 0
        // It monitors the error rate
        if (this.isChangeDetected || this.isInitialized == false) {
            resetLearning();
            this.isInitialized = true;
        }

        this.isChangeDetected = false;
        this.isWarningZone = false;

        while (actualPrediction.size() < tamanhoJanela - 1) {
            actualPrediction.add(prediction);
            return;
        }

        actualPrediction.add(prediction);
        if (expectedPrediction.isEmpty()) {
            expectedPrediction.addAll(actualPrediction);
            actualPrediction.clear();
            return;
        }

        ArrayList<Double> expectedPercentages = getPercentages(expectedPrediction);
        ArrayList<Double> actualPercentages = getPercentages(actualPrediction);

        System.out.println(getPercentages(expectedPrediction));
        System.out.println(getPercentages(actualPrediction));

        psi = 0.0;

        // Calcular o PSI usando a fórmula
        for (int i = 0; i < expectedPercentages.size(); i++) {
            if (actualPercentages.get(i) == 0) {
                psi += 0;
            } else {
                psi += (expectedPercentages.get(i) - actualPercentages.get(i))
                        * Math.log(expectedPercentages.get(i) / actualPercentages.get(i));
            }
        }

        System.out.println(psi);

        expectedPrediction.clear();
        expectedPrediction.addAll(actualPrediction);
        actualPrediction.clear();

        if (psi >=0.2) {
            this.isChangeDetected = true;
        } else if (psi >=0.1) {
            this.isWarningZone = true;
        } else {
            this.isWarningZone = false;
        }

        System.out.println(isChangeDetected);
    }

    @Override
    public void getDescription(StringBuilder sb, int indent) {
        // TODO Auto-generated method stub
    }

    @Override
    protected void prepareForUseImpl(TaskMonitor monitor,
            ObjectRepository repository) {
        // TODO Auto-generated method stub
    }

    private static ArrayList<Double> getPercentages(ArrayList<Double> values) {
        ArrayList<Double> percentages = new ArrayList<>();
        List<List<Double>> partition = Lists.partition(values, values.size() / 10);

        double sum = 0;

        for (int i = 0; i < partition.size(); i++) {
            for (int j = 0; j < partition.get(i).size(); j++) {
                sum += partition.get(i).get(j);
            }
        }

        for (int i = 0; i < partition.size(); i++) {
            double sum2 = 0;
            for (int j = 0; j < partition.get(i).size(); j++) {
                sum2 += partition.get(i).get(j);
            }
            //System.out.println(sum2 + " / " + sum +  " = " + sum2 / sum);
            if (sum2 / sum == 0.0) {
                percentages.add(0.0001);
            } else {
                percentages.add(sum2 / sum);
            }
        }

        // Retornar uma lista de porcentagens
        return percentages;

    }
}
