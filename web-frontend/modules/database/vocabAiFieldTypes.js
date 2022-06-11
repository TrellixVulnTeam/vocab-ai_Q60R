import { FieldType } from '@baserow/modules/database/fieldTypes'

import FieldTextSubForm from '@baserow/modules/database/components/field/FieldTextSubForm'
import GridViewFieldText from '@baserow/modules/database/components/view/grid/fields/GridViewFieldText'
import RowEditFieldText from '@baserow/modules/database/components/row/RowEditFieldText'

export class TranslationFieldType extends FieldType {
  static getType() {
    return 'translation'
  }

  getIconClass() {
    return 'list-ol'
  }

  getName() {
    return 'Translation'
  }

  getFormComponent() {
    return FieldTextSubForm
  }

  getGridViewFieldComponent() {
    return GridViewFieldText
  }

  getRowEditFieldComponent() {
    return RowEditFieldText
  }
}