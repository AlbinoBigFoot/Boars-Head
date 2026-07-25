-- Lightspeed AdhocTrend / user-saved trends schema (Microsoft SQL Server)
-- Required by named queries under ignition/named-query/AdhocTrend/*
-- Database connection name in resource.json: "ignition"

IF OBJECT_ID(N'dbo.adhoc_trend_configs', N'U') IS NULL
BEGIN
    CREATE TABLE dbo.adhoc_trend_configs (
        id              INT IDENTITY(1, 1) NOT NULL
            CONSTRAINT PK_adhoc_trend_configs PRIMARY KEY,
        username        NVARCHAR(255) NOT NULL,
        trend_name      NVARCHAR(255) NOT NULL,
        trend_config    NVARCHAR(MAX) NOT NULL,  -- JSON text (session.custom.AdhocTrend)
        is_shared       BIT NOT NULL
            CONSTRAINT DF_adhoc_trend_configs_is_shared DEFAULT (0),
        created_at      DATETIME2(3) NOT NULL
            CONSTRAINT DF_adhoc_trend_configs_created DEFAULT (SYSUTCDATETIME()),
        updated_at      DATETIME2(3) NOT NULL
            CONSTRAINT DF_adhoc_trend_configs_updated DEFAULT (SYSUTCDATETIME()),
        CONSTRAINT UQ_adhoc_trend_configs_username_trend_name
            UNIQUE (username, trend_name)
    );
END
GO

IF NOT EXISTS (
    SELECT 1
    FROM sys.indexes
    WHERE name = N'IX_adhoc_trend_configs_username'
      AND object_id = OBJECT_ID(N'dbo.adhoc_trend_configs')
)
BEGIN
    CREATE NONCLUSTERED INDEX IX_adhoc_trend_configs_username
        ON dbo.adhoc_trend_configs (username);
END
GO

IF NOT EXISTS (
    SELECT 1
    FROM sys.indexes
    WHERE name = N'IX_adhoc_trend_configs_shared'
      AND object_id = OBJECT_ID(N'dbo.adhoc_trend_configs')
)
BEGIN
    CREATE NONCLUSTERED INDEX IX_adhoc_trend_configs_shared
        ON dbo.adhoc_trend_configs (is_shared)
        WHERE is_shared = 1;
END
GO
