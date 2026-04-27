select
    date(created_at) as event_date,
    count(*) as total_events,
    avg(value) as avg_value
from {{ ref('stg_data') }}
group by event_date