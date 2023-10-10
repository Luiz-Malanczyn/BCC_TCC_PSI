package moa.classifiers.core.driftdetection;

import com.github.javacliparser.FloatOption;
import com.github.javacliparser.IntOption;
import com.google.common.collect.Lists;
import gnu.trove.impl.sync.TSynchronizedShortObjectMap;
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

    //private static final int DDM_MINNUMINST = 30;
    public IntOption minNumInstancesOption = new IntOption(
            "minNumInstances",
            'n',
            "The minimum number of instances before permitting detecting change.",
            100, 0, Integer.MAX_VALUE);

    public FloatOption warningLevelOption = new FloatOption(
            "warningLevel", 'w', "Warning Level.",
            0.2, 0.0, 1.0);

    public FloatOption outcontrolLevelOption = new FloatOption(
            "outcontrolLevel", 'o', "Outcontrol Level.",
            0.3, 0.0, 1.0);

    public IntOption tamanhoJanelaOption = new IntOption(
            "tamanhoJanela",
            't',
            "The minimum number of instances before permitting detecting change.",
            1000, 0, Integer.MAX_VALUE);

    public IntOption tamanhoBinOption = new IntOption(
            "tamanhoBin",
            'b',
            "The number of bins to split the window.",
            10, 1, 100);

    private int numInstances = 1;

    private int minNumInstances;

    private double warningLevel;

    private double outcontrolLevel;

    private int tamanhoJanela;

    private int tamanhoBin;

    private Double psi;

    public PSI() {
        resetLearning();
    }

    public ArrayList<Double> actualPrediction = new ArrayList<Double>();

    public ArrayList<Double> expectedPrediction = new ArrayList<Double>();

    @Override
    public void resetLearning() {
        psi = 0.0;
        numInstances = 1;
        actualPrediction.clear();
        expectedPrediction.clear();
        minNumInstances = this.minNumInstancesOption.getValue();
        warningLevel = this.warningLevelOption.getValue();
        outcontrolLevel = this.outcontrolLevelOption.getValue();
        tamanhoJanela = this.tamanhoJanelaOption.getValue();
        tamanhoBean = this.tamanhoBeanOption.getValue();
    }

    @Override
    public void input(double prediction) {
        // prediction must be 1 or 0
        // It monitors the error rate
        if (this.isChangeDetected || this.isInitialized == false) {
            resetLearning();
            this.isInitialized = true;
        }

        numInstances++;

        this.isChangeDetected = false;
        this.isWarningZone = false;

        if (actualPrediction.size() < tamanhoJanela - 1) {
            actualPrediction.add(prediction);
            return;
        }

        actualPrediction.add(prediction);
        if (expectedPrediction.isEmpty()) {
            expectedPrediction.addAll(actualPrediction);
            actualPrediction.clear();
            return;
        }

        if (numInstances < minNumInstances) {
            return;
        }

        ArrayList<Double> expectedPercentages = getPercentages(expectedPrediction);
        ArrayList<Double> actualPercentages = getPercentages(actualPrediction);

        //System.out.println(getPercentages(expectedPrediction));
        //System.out.println(getPercentages(actualPrediction));


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

        if (psi >= outcontrolLevel) {
            this.isChangeDetected = true;
            //System.out.println(numInstances);
            //System.out.println(psi);
        } else if (psi >= warningLevel) {
            this.isWarningZone = true;
            //System.out.println(numInstances);
            //System.out.println(psi);
        } else {
            this.isWarningZone = false;
        }

        //System.out.println(psi);

        expectedPrediction.remove(0);
        expectedPrediction.add(actualPrediction.get(0));
        actualPrediction.remove(0);

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

    private ArrayList<Double> getPercentages(ArrayList<Double> values) {
        ArrayList<Double> percentages = new ArrayList<>();
        List<List<Double>> partition = Lists.partition(values, values.size() / tamanhoBean);

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
