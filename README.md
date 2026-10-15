# Airflow Project 2

Bu layihə Apache Airflow, PostgreSQL və MinIO inteqrasiyasını Docker mühitində öyrənmək və tətbiq etmək üçün hazırlanmışdır.

## İstifadə Olunan Texnologiyalar

- **Apache Airflow 3.1.0** — İş axınlarının idarə edilməsi və DAG-ların icrası
- **Python** — DAG və tapşırıqların yazılması
- **PostgreSQL 16** — Verilənlər bazası ilə əlaqə
- **MinIO** — Obyekt yaddaşının idarə edilməsi
- **Docker & Docker Compose** — Xidmətlərin konteynerlərdə işə salınması

## Layihənin Strukturu

```text
airflowproject2/
├── airflow/
│   └── dags/
│       ├── first.py
│       └── second.py
├── screenshot/
├── docker-compose.yaml
├── Dockerfile
├── requirements.txt
└── .gitignore
```

## Layihənin İmkanları

- Airflow-da DAG-ların yaradılması və icrası.
- `PostgresHook` vasitəsilə PostgreSQL-ə qoşulma və SQL sorğularının icrası.
- MinIO Client (`mc`) vasitəsilə MinIO bağlantısının konfiqurasiyası.
- Faylların MinIO-ya yüklənməsi və yoxlanılması.
- Tapşırıqların icra nəticələrinin loglar vasitəsilə izlənilməsi.

## DAG-lar

**1. `mc-alias-dag`**

MinIO alias-ını konfiqurasiya edir, nümunə faylı yaradır, MinIO-ya yükləyir, obyektləri siyahıya alır və yüklənməni yoxlayır.

**2. `Postgres_Hook`**

Airflow-da yaradılmış `pg_conn_id` bağlantısından istifadə edərək `PostgresHook` vasitəsilə `SELECT 1` SQL sorğusunu icra edir.

## İşə Salınma

### 1. Repozitoriyanı klonlayın

```bash
git clone https://github.com/muradnajiyev/airflowproject2.git
cd airflowproject2
```

### 2. Mühit dəyişənlərini konfiqurasiya edin

Layihənin əsas qovluğunda `.env` faylı yaradın və tələb olunan Airflow və PostgreSQL dəyişənlərini əlavə edin.

### 3. Konteynerləri başladın

```bash
docker compose up --build -d
```

### 4. Xidmətlərə daxil olun

- **Airflow:** [http://localhost:8081](http://localhost:8081)
- **MinIO Console:** [http://localhost:9003](http://localhost:9003)

PostgreSQL DAG-ını icra etməzdən əvvəl Airflow interfeysində `pg_conn_id` adlı PostgreSQL Connection yaradın.

## Ekran Görüntüləri

`screenshot/` qovluğunda tapşırıqların icrasını, logları və MinIO interfeysini əks etdirən görüntülər yerləşir.

## Müəllif

**Murad Najiyev**

GitHub: [@muradnajiyev](https://github.com/muradnajiyev)
