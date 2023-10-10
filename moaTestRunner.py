import subprocess
import numpy as np
import csv
import os

class Runner:
    sizeOfAg = ''
    sizeOfAg_path = ''
    jar = ''
    jar_path = ''
    heap_max_size = ''
    line_result_matrix = []
    csvTitle = ""
    csv_head = []

    def __init__(self):
        print("inicio...")
        self.set_start_param()

    def set_start_param(self):
        self.sizeOfAg_path = 'C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\sizeofag-1.0.4.jar'
        self.jar_path = 'C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-release-2023.04.0-bin\\moa-release-2023.04.0\\lib\\moa-tcc.jar'
        self.heap_max_size = '-Xmx6g'
        
    def testAbrupt(self, window='100', warning='0.1', change='0.2'):
        result = subprocess.Popen('java -cp '+self.jar_path+' -javaagent:'+self.sizeOfAg_path+' moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d (PSI -w '+warning+' -o '+change+' -t '+window+')) -s (moa.streams.ArffFileStream -f C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\abrupt2.arff) -i 100000 -f 100000"', shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        print(last_line)
        self.line_result_matrix.append([last_line])


    def testGradual(self, window='100', warning='0.1', change='0.2'):
        result = subprocess.Popen('java -cp '+self.jar_path+' -javaagent:'+self.sizeOfAg_path+' moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d (PSI -w '+warning+' -o '+change+' -t '+window+')) -s (moa.streams.ArffFileStream -f C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\gradual2.arff) -i 100000 -f 100000"', shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        print(last_line)
        self.line_result_matrix.append([last_line])

    def test(self, window='100', warning='0.1', change='0.2'):
        self.csv_head = ['Learning evaluation instances', 'Evaluation time', 'Model cost', 'Learned instances', 'Detected changes', 'Detected Warnings', 'Predicion error', 'True changes', 'Delay detection', 'True changes detected', 'Input values', 'Model training instances', 'Model serialized size']
        self.testAbrupt(window, warning, change)
        self.testGradual(window, warning, change)

    def test_other_detectors(self):
        self.csv_head = ['Learning evaluation instances', 'Evaluation time', 'Model cost', 'Learned instances', 'Detected changes', 'Detected Warnings', 'Predicion error', 'True changes', 'Delay detection', 'True changes detected', 'Input values', 'Model training instances', 'Model serialized size']
        ddm_abrupt = subprocess.Popen('java -cp '+self.jar_path+' -javaagent:'+self.sizeOfAg_path+' moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d DDM) -s (moa.streams.ArffFileStream -f C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\abrupt2.arff) -i 100000 -f 100000"',shell=True, stdout=subprocess.PIPE).stdout
        eddm_abrupt = subprocess.Popen('java -cp '+self.jar_path+' -javaagent:'+self.sizeOfAg_path+' moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d EDDM) -s (moa.streams.ArffFileStream -f C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\abrupt2.arff) -i 100000 -f 100000"',shell=True, stdout=subprocess.PIPE).stdout
        adwin_abrupt = subprocess.Popen('java -cp '+self.jar_path+' -javaagent:'+self.sizeOfAg_path+' moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d ADWINChangeDetector) -s (moa.streams.ArffFileStream -f C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\abrupt2.arff) -i 100000 -f 100000"',shell=True, stdout=subprocess.PIPE).stdout
        cusum_abrupt = subprocess.Popen('java -cp '+self.jar_path+' -javaagent:'+self.sizeOfAg_path+' moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d CusumDM) -s (moa.streams.ArffFileStream -f C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\abrupt2.arff) -i 100000 -f 100000"',shell=True, stdout=subprocess.PIPE).stdout
        page_abrupt = subprocess.Popen('java -cp '+self.jar_path+' -javaagent:'+self.sizeOfAg_path+' moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d PageHinkleyDM) -s (moa.streams.ArffFileStream -f C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\abrupt2.arff) -i 100000 -f 100000"',shell=True, stdout=subprocess.PIPE).stdout

        ddm_grad = subprocess.Popen('java -cp '+self.jar_path+' -javaagent:'+self.sizeOfAg_path+' moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d DDM) -s (moa.streams.ArffFileStream -f C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\gradual2.arff) -i 100000 -f 100000"',shell=True, stdout=subprocess.PIPE).stdout
        eddm_grad = subprocess.Popen('java -cp '+self.jar_path+' -javaagent:'+self.sizeOfAg_path+' moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d EDDM) -s (moa.streams.ArffFileStream -f C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\gradual2.arff) -i 100000 -f 100000"',shell=True, stdout=subprocess.PIPE).stdout
        adwin_grad = subprocess.Popen('java -cp '+self.jar_path+' -javaagent:'+self.sizeOfAg_path+' moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d ADWINChangeDetector) -s (moa.streams.ArffFileStream -f C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\gradual2.arff) -i 100000 -f 100000"',shell=True, stdout=subprocess.PIPE).stdout
        cusum_grad = subprocess.Popen('java -cp '+self.jar_path+' -javaagent:'+self.sizeOfAg_path+' moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d CusumDM) -s (moa.streams.ArffFileStream -f C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\gradual2.arff) -i 100000 -f 100000"',shell=True, stdout=subprocess.PIPE).stdout
        page_grad = subprocess.Popen('java -cp '+self.jar_path+' -javaagent:'+self.sizeOfAg_path+' moa.DoTask "EvaluateConceptDrift -l (ChangeDetectorLearner -d PageHinkleyDM) -s (moa.streams.ArffFileStream -f C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\gradual2.arff) -i 100000 -f 100000"',shell=True, stdout=subprocess.PIPE).stdout

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

    def classifiers_only(self):
        result = subprocess.Popen(
            'java ' + self.heap_max_size + ' -cp '+self.jar_path+' -javaagent:'+self.sizeOfAg_path+' moa.DoTask "EvaluatePrequential -l bayes.NaiveBayes -s (ArffFileStream -f C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\sintetica\\SINE.arff) -e BasicClassificationPerformanceEvaluator -f 100000000 -q 100000000"',
            shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        self.line_result_matrix.append(last_line)

        result = subprocess.Popen(
            'java ' + self.heap_max_size + ' -cp '+self.jar_path+' -javaagent:'+self.sizeOfAg_path+' moa.DoTask "EvaluatePrequential -l trees.HoeffdingTree -s (ArffFileStream -f C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\sintetica\\SINE.arff) -e BasicClassificationPerformanceEvaluator -f 100000000 -q 100000000"',
            shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        self.line_result_matrix.append(last_line)

        result = subprocess.Popen(
            'java ' + self.heap_max_size + ' -cp '+self.jar_path+' -javaagent:'+self.sizeOfAg_path+' moa.DoTask "EvaluatePrequential -l trees.HoeffdingTree -s (ArffFileStream -f C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\sintetica\\SINE.arff) -e BasicClassificationPerformanceEvaluator -f 100000000 -q 100000000"',
            shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        self.line_result_matrix.append(last_line)

        for i in self.line_result_matrix:
            print(i)

    def iterate_streams(self, classifier, folder_path):
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_path = file_path.replace('\\','\\\\')
                print("File:", file_path)
                if classifier == 'nb':
                    self.classifiers_detectors_nb(file_path)
                elif classifier == 'hof':
                    self.classifiers_detectors_hTree(file_path)
                elif classifier == 'arf':
                    self.classifiers_detectors_randomForest(file_path)
                else:
                    print("Opcao invalida de classificador")

    def classifiers_detectors_nb(self, file_path):
        self.line_result_matrix.clear()
        file_name = file_path
        self.csv_head = ['learning evaluation instances','evaluation time (cpu seconds)','model cost (RAM-Hours)','classified instances','classifications correct (percent)','Kappa Statistic (percent)','Kappa Temporal Statistic (percent)','Kappa M Statistic (percent)','model training instances','model serialized size (bytes)','Change detected','Warning detected']
        result = subprocess.Popen(
            'java ' + self.heap_max_size + ' -cp ' + self.jar_path + ' -javaagent:' + self.sizeOfAg_path + ' moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -d ADWINChangeDetector) -s (ArffFileStream -f '+file_path+') -e BasicClassificationPerformanceEvaluator -f 100000000 -q 100000000"',
            shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        self.line_result_matrix.append(last_line)

        result = subprocess.Popen(
            'java ' + self.heap_max_size + ' -cp ' + self.jar_path + ' -javaagent:' + self.sizeOfAg_path + ' moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -d CusumDM) -s (ArffFileStream -f '+file_path+') -e BasicClassificationPerformanceEvaluator -f 100000000 -q 100000000"',
            shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        self.line_result_matrix.append(last_line)

        result = subprocess.Popen(
            'java ' + self.heap_max_size + ' -cp ' + self.jar_path + ' -javaagent:' + self.sizeOfAg_path + ' moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -d DDM) -s (ArffFileStream -f '+file_path+') -e BasicClassificationPerformanceEvaluator -f 100000000 -q 100000000"',
            shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        self.line_result_matrix.append(last_line)

        result = subprocess.Popen(
            'java ' + self.heap_max_size + ' -cp ' + self.jar_path + ' -javaagent:' + self.sizeOfAg_path + ' moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -d EDDM) -s (ArffFileStream -f '+file_path+') -e BasicClassificationPerformanceEvaluator -f 100000000 -q 100000000"',
            shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        self.line_result_matrix.append(last_line)

        result = subprocess.Popen(
            'java ' + self.heap_max_size + ' -cp ' + self.jar_path + ' -javaagent:' + self.sizeOfAg_path + ' moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -d PageHinkleyDM) -s (ArffFileStream -f '+file_path+') -e BasicClassificationPerformanceEvaluator -f 100000000 -q 100000000"',
            shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        self.line_result_matrix.append(last_line)

        result = subprocess.Popen(
            'java ' + self.heap_max_size + ' -cp ' + self.jar_path + ' -javaagent:' + self.sizeOfAg_path + ' moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -d PSI) -s (ArffFileStream -f '+file_path+') -e BasicClassificationPerformanceEvaluator -f 100000000 -q 100000000"',
            shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        self.line_result_matrix.append(last_line)

        for i in self.line_result_matrix:
            print(i)
        self.get_csv(file_name)

    def classifiers_detectors_hTree(self, file_path):
        self.line_result_matrix.clear()
        file_name = file_path
        self.csv_head=['learning evaluation instances','evaluation time (cpu seconds)','model cost (RAM-Hours)','classified instances','classifications correct (percent)','Kappa Statistic (percent)','Kappa Temporal Statistic (percent)','Kappa M Statistic (percent)','model training instances','model serialized size (bytes)','Change detected','Warning detected','tree size (nodes)','tree size (leaves)','active learning leaves','tree depth','active leaf byte size estimate','inactive leaf byte size estimate','byte size estimate overhead','maximum prediction paths used']
        result = subprocess.Popen(
            'java ' + self.heap_max_size + ' -cp ' + self.jar_path + ' -javaagent:' + self.sizeOfAg_path + ' moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l trees.HoeffdingOptionTree -d ADWINChangeDetector) -s (ArffFileStream -f '+file_path+') -e BasicClassificationPerformanceEvaluator -f 100000000 -q 100000000"',
            shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        self.line_result_matrix.append(last_line)

        result = subprocess.Popen(
            'java ' + self.heap_max_size + ' -cp ' + self.jar_path + ' -javaagent:' + self.sizeOfAg_path + ' moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l trees.HoeffdingOptionTree -d CusumDM) -s (ArffFileStream -f '+file_path+') -e BasicClassificationPerformanceEvaluator -f 100000000 -q 100000000"',
            shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        self.line_result_matrix.append(last_line)

        result = subprocess.Popen(
            'java ' + self.heap_max_size + ' -cp ' + self.jar_path + ' -javaagent:' + self.sizeOfAg_path + ' moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l trees.HoeffdingOptionTree -d DDM) -s (ArffFileStream -f '+file_path+') -e BasicClassificationPerformanceEvaluator -f 100000000 -q 100000000"',
            shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        self.line_result_matrix.append(last_line)

        result = subprocess.Popen(
            'java ' + self.heap_max_size + ' -cp ' + self.jar_path + ' -javaagent:' + self.sizeOfAg_path + ' moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l trees.HoeffdingOptionTree -d EDDM) -s (ArffFileStream -f '+file_path+') -e BasicClassificationPerformanceEvaluator -f 100000000 -q 100000000"',
            shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        self.line_result_matrix.append(last_line)

        result = subprocess.Popen(
            'java ' + self.heap_max_size + ' -cp ' + self.jar_path + ' -javaagent:' + self.sizeOfAg_path + ' moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l trees.HoeffdingOptionTree -d PageHinkleyDM) -s (ArffFileStream -f '+file_path+') -e BasicClassificationPerformanceEvaluator -f 100000000 -q 100000000"',
            shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        self.line_result_matrix.append(last_line)

        result = subprocess.Popen(
            'java ' + self.heap_max_size + ' -cp ' + self.jar_path + ' -javaagent:' + self.sizeOfAg_path + ' moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l trees.HoeffdingOptionTree -d PSI) -s (ArffFileStream -f '+file_path+') -e BasicClassificationPerformanceEvaluator -f 100000000 -q 100000000"',
            shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        self.line_result_matrix.append(last_line)

        for i in self.line_result_matrix:
            print(i)
        self.get_csv(file_name)

    def classifiers_detectors_randomForest(self, file_path):
        self.line_result_matrix.clear()
        file_name = file_path
        self.csv_head = ['learning evaluation instances','evaluation time (cpu seconds)','model cost (RAM-Hours)','classified instances','classifications correct (percent)','Kappa Statistic (percent)','Kappa Temporal Statistic (percent)','Kappa M Statistic (percent)','model training instances','model serialized size (bytes)','Change detected','Warning detected','[avg] model training instances','[err] model training instances','[avg] model serialized size (bytes)','[err] model serialized size (bytes)','[avg] tree size (nodes)','[err] tree size (nodes)','[avg] tree size (leaves)','[err] tree size (leaves)','[avg] active learning leaves','[err] active learning leaves','[avg] tree depth','[err] tree depth','[avg] active leaf byte size estimate','[err] active leaf byte size estimate','[avg] inactive leaf byte size estimate','[err] inactive leaf byte size estimate','[avg] byte size estimate overhead','[err] byte size estimate overhead']
        result = subprocess.Popen(
            'java ' + self.heap_max_size + ' -cp ' + self.jar_path + ' -javaagent:' + self.sizeOfAg_path + ' moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l trees.HoeffdingOptionTree -d ADWINChangeDetector) -s (ArffFileStream -f '+file_path+') -e BasicClassificationPerformanceEvaluator -f 100000000 -q 100000000"',
            shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        self.line_result_matrix.append(last_line)

        result = subprocess.Popen(
            'java ' + self.heap_max_size + ' -cp ' + self.jar_path + ' -javaagent:' + self.sizeOfAg_path + ' moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l trees.HoeffdingOptionTree -d CusumDM) -s (ArffFileStream -f '+file_path+') -e BasicClassificationPerformanceEvaluator -f 100000000 -q 100000000"',
            shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        self.line_result_matrix.append(last_line)

        result = subprocess.Popen(
            'java ' + self.heap_max_size + ' -cp ' + self.jar_path + ' -javaagent:' + self.sizeOfAg_path + ' moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l trees.HoeffdingOptionTree -d DDM) -s (ArffFileStream -f '+file_path+') -e BasicClassificationPerformanceEvaluator -f 100000000 -q 100000000"',
            shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        self.line_result_matrix.append(last_line)

        result = subprocess.Popen(
            'java ' + self.heap_max_size + ' -cp ' + self.jar_path + ' -javaagent:' + self.sizeOfAg_path + ' moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l trees.HoeffdingOptionTree -d EDDM) -s (ArffFileStream -f '+file_path+') -e BasicClassificationPerformanceEvaluator -f 100000000 -q 100000000"',
            shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        self.line_result_matrix.append(last_line)

        result = subprocess.Popen(
            'java ' + self.heap_max_size + ' -cp ' + self.jar_path + ' -javaagent:' + self.sizeOfAg_path + ' moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l trees.HoeffdingOptionTree -d PageHinkleyDM) -s (ArffFileStream -f '+file_path+') -e BasicClassificationPerformanceEvaluator -f 100000000 -q 100000000"',
            shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        self.line_result_matrix.append(last_line)

        result = subprocess.Popen(
            'java ' + self.heap_max_size + ' -cp ' + self.jar_path + ' -javaagent:' + self.sizeOfAg_path + ' moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l trees.HoeffdingOptionTree -d PSI) -s (ArffFileStream -f '+file_path+') -e BasicClassificationPerformanceEvaluator -f 100000000 -q 100000000"',
            shell=True, stdout=subprocess.PIPE).stdout
        last_line = result.readlines()[-1].decode().strip()
        self.line_result_matrix.append(last_line)

        for i in self.line_result_matrix:
            print(i)
        self.get_csv(file_name)

    def get_csv(self, csv_title):
        arr = np.asarray(self.line_result_matrix)
        with open('C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-results\\'+csv_title+'.csv', 'w') as f:
            f.truncate()
            writer = csv.writer(f, delimiter=',')
            writer.writerow(self.csv_head)
            writer.writerows(arr)
        self.clean_csv(csv_title)

    def clean_csv(self,csv_title):
        input_file = 'C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-results\\'+csv_title+'.csv'
        output_file = 'C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-results\\'+csv_title+'_clean.csv'
        with open(input_file, 'r') as f, open(output_file, 'w') as new_f:
            for line in f:
                cleaned_line = line.replace('"', '').replace("'", '')
                new_f.write(cleaned_line)


run = Runner()
#Testes de tuning dos thresholds
#run.csvTitle = "tuningThresholds"
#run.test(warning='0.02', change='0.05')
#run.test(warning='0.02', change='0.10')
#run.test(warning='0.02', change='0.15')
#run.test(warning='0.02', change='0.20')
#run.test(warning='0.02', change='0.30')

#run.test(warning='0.05', change='0.10')
#run.test(warning='0.05', change='0.15')
#run.test(warning='0.05', change='0.20')
#run.test(warning='0.05', change='0.30')

#run.test(warning='0.10', change='0.15')
#run.test(warning='0.10', change='0.20')
#run.test(warning='0.10', change='0.30')

#run.test(warning='0.15', change='0.20')
#run.test(warning='0.15', change='0.30')

#run.test(warning='0.20', change='0.30')


#Testes de tuning do parametro janela
# run.csvTitle = "tuningWindow"
# run.test(window='100',warning='0.02', change='0.30')
# run.test(window='100',warning='0.05', change='0.30')
# run.test(window='100',warning='0.10', change='0.30')
# run.test(window='100',warning='0.15', change='0.30')
# run.test(window='100',warning='0.20', change='0.30')
#
# run.test(window='500',warning='0.02', change='0.30')
# run.test(window='500',warning='0.05', change='0.30')
# run.test(window='500',warning='0.10', change='0.30')
# run.test(window='500',warning='0.15', change='0.30')
# run.test(window='500',warning='0.20', change='0.30')
#
# run.test(window='1000',warning='0.02', change='0.30')
# run.test(window='1000',warning='0.05', change='0.30')
# run.test(window='1000',warning='0.10', change='0.30')
# run.test(window='1000',warning='0.15', change='0.30')
# run.test(window='1000',warning='0.20', change='0.30')

#run.csvTitle="aditionalTests"
#run.test(window='1000',warning='0.25', change='0.35')
#run.test(window='1000',warning='0.30', change='0.40')
#run.test(window='1000',warning='0.30', change='0.50')
#run.test(window='1000',warning='0.40', change='0.60')
#run.test(window='1000',warning='0.50', change='0.70')

#run.csvTitle = "otherDetectors"
#run.test_other_detectors()
#run.classifiers_detectors()

run.iterate_streams('C:\\Users\\gabri\\Documents\\faculdade\\2023\\TCC\\code\\moa-ARFFFiles\\sintetica')


#run.get_csv()
#run.clean_csv()

