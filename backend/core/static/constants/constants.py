# Sleep period = 2 seconds
SLEEP_PER = 2
# History years
HISTORY_YEARS = 0.05
# History days 
HISTORY_DAYS = 7
# market_types
MARKET_TYPES = (
    ('FX', 'FOREX'),
    ('EQUITY', 'EQUITY'),
    ('DEPT', 'DEPT'),
    ('DERIVATIVES', 'DERIVATIVES'),
)

SERVICES = (
    ('SUPPORT', 'SUPPORT'),
    ('MODELS', 'MODELS'),
    ('USER_EXPERIENCE', 'USER EXPERIENCE'),
    ('TECHNICAL', 'TECHNICAL'),
)

PAYMENT_METHOD = (
        ('BANK_TRANSFER', ('bank transfer')),
        ('CASH', ('cash')),
        ('CASH_ON_DELIVERY', ('cash on delivery')),
        ('PAYMENT_CARD', ('payment card'))
    )
FREQUENCY = (
        ('DAILY', ('daily')),
        ('MONTHLY', ('monthly')),
        ('YEARLY', ('yearly'))
    )
STATUS = (
        ('NEW', ('new')),
        ('SENT', ('sent')),
        ('RETURNED', ('returned')),
        ('CANCELED', ('canceled')),
        ('PAID', ('paid')),
        ('CREDITED', ('credited')),
    )