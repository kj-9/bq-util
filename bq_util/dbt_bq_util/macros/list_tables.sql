
{% macro list_tables(table_prefix) %}
{% set relations = dbt_utils.get_relations_by_prefix(var('DATASET'), table_prefix) %}

{% for relation in relations %}
    {{ print("relations: " ~ relations) }}
{% endfor %}
{% endmacro %}
