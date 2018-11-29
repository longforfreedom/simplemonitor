use md;
create table smonitor_storage_info(
    hostname varchar(50),
    ip varchar(50),
    ts varchar(20),
    store_device varchar(100),
    store_mountpoint varchar(50),
    store_total bigint,
    store_free bigint,
    store_used bigint, 
    percent float
)DEFAULT CHARSET=utf8;


----------------------统一记录到一张表中------------------------------
create table smonitor_metrics(
    hostname varchar(50),
    ip varchar(50),
    ts varchar(20),
    metric varchar(200),
    val varchar(100)
)DEFAULT CHARSET=utf8;
