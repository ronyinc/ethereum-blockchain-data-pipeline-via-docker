

select
    address,
    block_number,
    block_timestamp,
    bytecode,
    date,
    last_modified

from {{ source('eth', 'contracts')}}

{{ dev_row_filter('date') }}