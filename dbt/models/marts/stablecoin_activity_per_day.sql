
{{ config( tags=['stablecoin'], grants = {'+select': ['TESTER']} )  }}

select
		t.date,
		t.token_address,
		s.type,
		s.symbol,

		 {{ conversion('t.value', 's.decimals') }}  as total_value 

from {{ ref('stg_token_transfers') }} t

left join 
           {{  ref('stablecoins') }} s on  t.token_address = s.contract_address
group by 
		t.date,
		t.token_address,
		s.type,
		s.symbol

-- {{ random_macro() }}
