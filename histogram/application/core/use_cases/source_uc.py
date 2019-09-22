from application.core.exceptions.plain_data import PlanDataProcessNotSupport
from application.data_provider import SourceProvider, ParserProvider
from application.core.entities import HistogramEntity

class SourceUC(object):
    def __init__(self, data_source, data_format):
        self.source_provider = SourceProvider(data_source, data_format)
        self.parser_provider = ParserProvider()

    def to_histogram(self, params, element_type: str):
        resp_text = self.source_provider.get_plain_data(params)
        plain_list = self.parser_provider.execute(resp_text)
        try:
            return getattr(self, "to_histogram_%s" % element_type)(plain_list)
        except:
            raise PlanDataProcessNotSupport()
        
    def to_histogram_unique_words(self, plain_list): 
        #process make words
        #count words by unique  
        word_histogram = {}
        for w in plain_list:
            word_histogram[w] = word_histogram.get(w, 0)+1
        return HistogramEntity(word_histogram)