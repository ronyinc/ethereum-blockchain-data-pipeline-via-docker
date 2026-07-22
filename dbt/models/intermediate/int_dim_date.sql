{{ config(materialized='table') }}

with spine as (

{{
    dbt_utils.date_spine(
        datepart="day",
        start_date="cast('2020-01-01' as date)",
        end_date="cast(current_date as date)"
    )
}}

)

select

    cast(date_day as date)                  as date,
    year(date_day)                          as year,
    quarter(date_day)                       as quarter_number,
    'Q' || quarter(date_day)               as quarter_name,
    month(date_day)                         as month_number,
    monthname(date_day)                     as month_name,
    dayofmonth(date_day)                    as day_of_month,
    dayofweek(date_day)                     as day_of_week_number,
    dayname(date_day)                       as day_name,
    dayofyear(date_day)                     as day_of_year,
    weekofyear(date_day)                    as week_of_year,
    case when dayofweek(date_day) in (0, 6)
        then false else true
    end                                     as is_weekday

from spine