from optimizers import SVMOptimizer


class Pipeline:

    def __init__(self, preprocessor):
        self.sentences = None
        self.processed_sentences = None
        self.labels = None
        self.matrices = None
        self.vectors = None
        self.classifier = None
        self.preprocessor = preprocessor
        self.svm_optimizer = None

    def preprocess(self, verbose=True):
        self.sentences, self.processed_sentences, self.labels, self.matrices, self.vectors =\
            self.preprocessor.preprocess(verbose)
        self.svm_optimizer = SVMOptimizer(self.vectors, self.labels)
        return self

    def optimal_svm(self, results_file='svm_results.csv', verbose=True):
        self.classifier, config = self.svm_optimizer.optimal(results_file, verbose)
        return config
