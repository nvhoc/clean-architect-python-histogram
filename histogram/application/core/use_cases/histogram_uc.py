from application.core.entities import SourceEntity,HistogramEntity, CheckEntity
from application.core.use_cases import SourceUC
from application.data_provider import DatabaseProvider


class HistogramUC(object):
    def __init__(self, data_source, data_format, element_type, params):

        self.histogram_entity = HistogramEntity({})

        self.source_entity = SourceEntity(data_source, data_format, params)
        source_key = self.source_entity.get_key()
        key = params[source_key]

        self.collection_key = {'data_source': data_source,
                               'data_format': data_format,
                               'element_type': element_type,
                               'key': key}
        self.element_type = element_type
        self.params = params

        self.model = DatabaseProvider().get_model('histogram')
        self.source_uc = SourceUC(data_source, data_format)

    def get_in_db(self):
        histogram_data = self.model.get_histogram_by_key(self.collection_key)
        if histogram_data is None:
            return CheckEntity()

        self.histogram_entity = HistogramEntity(histogram_data)
        return CheckEntity().ok()

    def get_histogram(self):
        self.histogram_entity = self.source_uc.to_histogram(
            self.params, self.element_type)
        return self

    def storage(self):
        self.model.insert(self.collection_key, self.histogram_entity.get())
        return self

    def top(self):
        # if in storage
        # if not
        return self.histogram_entity.get()
