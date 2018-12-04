use md;
----------------------统一记录到一张表中------------------------------
create table smonitor_metrics(
    hostname varchar(50),
    ip varchar(50),
    ts varchar(20),
    metric varchar(200),
    val varchar(100)
)DEFAULT CHARSET=utf8;