{% set source_query %}
    select hash, value from {{ source('eth', 'transactions') }}
{% endset %}

{% set staging_query %}
    select hash, value from {{ ref('stg_transactions') }}
{% endset %}

{{ audit_helper.compare_column_values(
    a_query = source_query,
    b_query = staging_query,
    primary_key = 'hash',
    column_to_compare = 'value'
) }}