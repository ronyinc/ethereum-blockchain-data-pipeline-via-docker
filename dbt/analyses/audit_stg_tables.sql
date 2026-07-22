
{% set old_relation = ref('stg_transactions') %}
{% set new_relation = ref('stg_transactions')  %} ---swap this to your new version

{{
    audit_helper.compare_relations(
        a_relation = old_relation,
        b_relation  = new_relation,
        primary_key = 'hash'
    )
}}