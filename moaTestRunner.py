import subprocess
import os
import numpy as np
import csv

class Runner:
    sizeOfAg = ""
    sizeOfAg_path = ""
    jar = ""
    jar_path = ""
    line_result_matrix = []

    def __init__(self):
        print("inicio...")

    def testAbrupt(self, window='100', warning='0.1', change='0.2'):
        result = subprocess.Popen('java -cp C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\moa-tcc.jar -javaagent:C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\sizeofag-1.0.4.jar moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d (PSI -n '+window+' -w '+warning+' -o '+change+')) -i 100000 -d C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\tuningAbrupt3.arff"',shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        print(last_line)
        self.line_result_matrix.append([last_line])

    def testGradual(self, window='100', warning='0.1', change='0.2'):
        result = subprocess.Popen('java -cp C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\moa-tcc.jar -javaagent:C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\sizeofag-1.0.4.jar moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d (PSI -n '+window+' -w '+warning+' -o '+change+')) -i 100000 -d C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\tuningGradual2.arff"',shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        print(last_line)
        self.line_result_matrix.append([last_line])

    def test(self, window='100', warning='0.1', change='0.2'):
        self.testAbrupt(window, warning, change)
        self.testGradual(window, warning, change)

    def test_other_detectors(self):
        ddm_abrupt = subprocess.Popen('java -cp C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\moa-tcc.jar -javaagent:C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\sizeofag-1.0.4.jar moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d DDM) -i 100000 -d C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\tuningAbrupt3.arff"',shell=True, stdout=subprocess.PIPE).stdout
        eddm_abrupt = subprocess.Popen('java -cp C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\moa-tcc.jar -javaagent:C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\sizeofag-1.0.4.jar moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d EDDM) -i 100000 -d C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\tuningAbrupt3.arff"',shell=True, stdout=subprocess.PIPE).stdout
        adwin_abrupt = subprocess.Popen('java -cp C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\moa-tcc.jar -javaagent:C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\sizeofag-1.0.4.jar moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d ADWINChangeDetector) -i 100000 -d C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\tuningAbrupt3.arff"',shell=True, stdout=subprocess.PIPE).stdout
        cusum_abrupt = subprocess.Popen('java -cp C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\moa-tcc.jar -javaagent:C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\sizeofag-1.0.4.jar moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d CusumDM) -i 100000 -d C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\tuningAbrupt3.arff"',shell=True, stdout=subprocess.PIPE).stdout
        page_abrupt = subprocess.Popen('java -cp C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\moa-tcc.jar -javaagent:C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\sizeofag-1.0.4.jar moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d PageHinkleyDM) -i 100000 -d C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\tuningAbrupt3.arff"',shell=True, stdout=subprocess.PIPE).stdout

        ddm_grad = subprocess.Popen('java -cp C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\moa-tcc.jar -javaagent:C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\sizeofag-1.0.4.jar moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d DDM) -i 100000 -d C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\tuningGradual2.arff"',shell=True, stdout=subprocess.PIPE).stdout
        eddm_grad = subprocess.Popen('java -cp C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\moa-tcc.jar -javaagent:C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\sizeofag-1.0.4.jar moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d EDDM) -i 100000 -d C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\tuningGradual2.arff"',shell=True, stdout=subprocess.PIPE).stdout
        adwin_grad = subprocess.Popen('java -cp C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\moa-tcc.jar -javaagent:C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\sizeofag-1.0.4.jar moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d ADWINChangeDetector) -i 100000 -d C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\tuningGradual2.arff"',shell=True, stdout=subprocess.PIPE).stdout
        cusum_grad = subprocess.Popen('java -cp C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\moa-tcc.jar -javaagent:C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\sizeofag-1.0.4.jar moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d CusumDM) -i 100000 -d C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\tuningGradual2.arff"',shell=True, stdout=subprocess.PIPE).stdout
        page_grad = subprocess.Popen('java -cp C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\moa-tcc.jar -javaagent:C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\sizeofag-1.0.4.jar moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d PageHinkleyDM) -i 100000 -d C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\tuningGradual2.arff"',shell=True, stdout=subprocess.PIPE).stdout

        self.line_result_matrix.append([ddm_abrupt.readlines()[-1].decode().strip()])
        self.line_result_matrix.append([ddm_grad.readlines()[-1].decode().strip()])
        self.line_result_matrix.append([eddm_abrupt.readlines()[-1].decode().strip()])
        self.line_result_matrix.append([eddm_grad.readlines()[-1].decode().strip()])
        self.line_result_matrix.append([adwin_abrupt.readlines()[-1].decode().strip()])
        self.line_result_matrix.append([adwin_grad.readlines()[-1].decode().strip()])
        self.line_result_matrix.append([cusum_abrupt.readlines()[-1].decode().strip()])
        self.line_result_matrix.append([cusum_grad.readlines()[-1].decode().strip()])
        self.line_result_matrix.append([page_abrupt.readlines()[-1].decode().strip()])
        self.line_result_matrix.append([page_grad.readlines()[-1].decode().strip()])

        for i in self.line_result_matrix:
            print(i)

    def get_csv(self):
        arr = np.asarray(self.line_result_matrix)
        with open('C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-results\\result_tuned.csv', 'w') as f:
            f.truncate()
            writer = csv.writer(f, delimiter=',')
            writer.writerow(['Learning evaluation instances', 'Evaluation time', 'Model cost', 'Learned instances', 'Detected changes', 'Detected Warnings', 'Predicion error', 'True changes', 'Delay detection', 'True changes detected', 'Input values', 'Model training instances', 'Model serialized size'])
            writer.writerows(arr)


    def clean_csv(self):
        input_file = 'C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-results\\result_tuned.csv'
        output_file = 'C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-results\\result_tuned_clean.csv'
        with open(input_file, 'r') as f, open(output_file, 'w') as new_f:
            for line in f:
                cleaned_line = line.replace('"', '').replace("'", '')
                new_f.write(cleaned_line)


run = Runner()
#Testes de tuning dos thresholds
# run.test(warning='0.02', change='0.05')
# run.test(warning='0.02', change='0.10')
# run.test(warning='0.02', change='0.15')
# run.test(warning='0.02', change='0.20')
# run.test(warning='0.02', change='0.30')
#
# run.test(warning='0.05', change='0.10')
# run.test(warning='0.05', change='0.15')
# run.test(warning='0.05', change='0.20')
# run.test(warning='0.05', change='0.30')
#
# run.test(warning='0.10', change='0.15')
# run.test(warning='0.10', change='0.20')
# run.test(warning='0.10', change='0.30')
#
# run.test(warning='0.15', change='0.20')
# run.test(warning='0.15', change='0.30')
#
# run.test(warning='0.20', change='0.30')

#Testes de tuning do parametro janela
# run.test(window='100', warning='0.02', change='0.30')
# run.test(window='100', warning='0.05', change='0.30')
# run.test(window='100', warning='0.10', change='0.30')
# run.test(window='100', warning='0.15', change='0.30')
# run.test(window='100', warning='0.20', change='0.30')
#
# run.test(window='500', warning='0.02', change='0.30')
# run.test(window='500', warning='0.05', change='0.30')
# run.test(window='500', warning='0.10', change='0.30')
# run.test(window='500', warning='0.15', change='0.30')
# run.test(window='500', warning='0.20', change='0.30')
#
# run.test(window='1000', warning='0.02', change='0.30')
# run.test(window='1000', warning='0.05', change='0.30')
# run.test(window='1000', warning='0.10', change='0.30')
# run.test(window='1000', warning='0.15', change='0.30')
# run.test(window='1000', warning='0.20', change='0.30')
# run.test_other_detectors()
run.test(window='100', warning='0.10', change='0.30')
run.test(window='500', warning='0.10', change='0.30')
run.test(window='1000', warning='0.10', change='0.30')
run.get_csv()
run.clean_csv()
