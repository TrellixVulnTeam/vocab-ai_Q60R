from django.db import models
from django.core.exceptions import ValidationError

from rest_framework import serializers

from baserow.contrib.database.fields.registries import FieldType
from baserow.contrib.database.views.handler import ViewHandler

from .vocabai_models import TranslationField

import logging
logger = logging.getLogger(__name__)


class TranslationTextField(models.TextField):
    requires_refresh_after_update = True

class TranslationFieldType(FieldType):
    type = "translation"
    model_class = TranslationField
    allowed_fields = ['source_field']
    serializer_field_names = ['source_field']

    can_be_primary_field = False

    def prepare_value_for_db(self, instance, value):
        return value

    def get_serializer_field(self, instance, **kwargs):
        return serializers.CharField(
            **{
                "required": False,
                "allow_null": True,
                "allow_blank": True,
                **kwargs,
            }        
        )

    def get_model_field(self, instance, **kwargs):
        return TranslationTextField(
            default=None,
            blank=True, 
            null=True, 
            **kwargs
        )

    def get_field_dependencies(self, field_instance, field_lookup_cache):
        logger.info(f'get_field_dependencies')
        return [field_instance.source_field]

    def row_of_dependency_updated(
        self,
        field,
        starting_row,
        update_collector,
        via_path_to_starting_table,
    ):
        logger.info(f'row_of_dependency_updated, row: {starting_row}, {type(starting_row)}')

        # source_value = getattr(starting_row, field.source_field)
        source_value = getattr(starting_row, 'field_1992')
        translated_value = 'translation: ' + source_value
        
        logger.info(f'translated_value: {translated_value}')

        logger.info(f'update_collector: {update_collector} type: {type(update_collector)}')


        update_collector.add_field_with_pending_update_statement(
            field,
            translated_value,
            via_path_to_starting_table=via_path_to_starting_table,
        )        

        super().row_of_dependency_updated(
            field,
            starting_row,
            update_collector,
            via_path_to_starting_table,
        )        

