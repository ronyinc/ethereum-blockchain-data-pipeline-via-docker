select
        {{ dbt_utils.generate_surrogate_key(['transaction_hash','log_index']) }} as transfer_id,
        transaction_hash,
        date,
        token_address,
        value

from {{ source('eth','token_transfers')}}

{{ dev_row_filter('date') }}