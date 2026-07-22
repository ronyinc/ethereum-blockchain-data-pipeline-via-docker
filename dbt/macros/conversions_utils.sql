{% macro ethereum_conversion(column_name) %}

   {{ column_name }}/1e18

{% endmacro %}


{% macro stablecoin_conversion(column_name)%}

   {{ column_name }}/1e6

{% endmacro %}


{% macro conversion(column_name, factor) %}

sum( {{column_name}}/power(10, {{ factor }} ))

{% endmacro %}


{% macro random_macro() %}

  {% set query %}

     select 
        distinct
        date
     from {{ref('stg_token_transfers')}}

  {% endset %}

  {% set sql = [] %}

  {% if execute %}

    {% set results = run_query(query) %}
    {% set result_list = results.columns[0].values() %}

    {% set sql = [] %}

    {% for i in result_list %}

       {% do sql.append("'"~i~"'") %}

    {% endfor %}   


    {# {{ log(query, info = True) }} #}
    {# {{ log(results, info =  True) }} #}
    {# {{ log(sql, info =  True) }} #}
    {# {{  log(sql | join(','), info=True) }} #}

  {% else %}

      {% set result_list = [] %}

  {%  endif %}

  {{ return(sql | join(','))}}

  
{% endmacro %}