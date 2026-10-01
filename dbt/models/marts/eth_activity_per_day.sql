
{{ config(tags=['eth']) }}

---  testing slim ci build --va-05

select
        date,
        transaction_category,
        count(*) as transaction_count,
        sum({{ ethereum_conversion('value') }}) as sum_ethereum_val

from 
         {{ ref('int_transactions_enriched') }}
group by 
        date,
        transaction_category