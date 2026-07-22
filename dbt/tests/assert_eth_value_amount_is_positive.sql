select
    sum(value) as total_amount
from {{ ref('stg_transactions_enriched') }}

having total_amount < 0