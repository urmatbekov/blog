from django.utils.encoding import force_text
from rest_framework.metadata import SimpleMetadata
from rest_framework.relations import RelatedField, ManyRelatedField


class MyMetaData(SimpleMetadata):

    def get_field_info(self, field):
        field_info = super(MyMetaData, self).get_field_info(field)
        if isinstance(field, (RelatedField, ManyRelatedField)):
            field_info['choices'] = [
                {
                    'value': choice_value,
                    'display_name': force_text(choice_name, strings_only=True)
                }
                for choice_value, choice_name in field.get_choices().items()
            ]
        return field_info
