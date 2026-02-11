# Skill: /bp-research (시장조사 및 데이터 수집)

## Purpose
조지아 트빌리시 K-Food 시장에 대한 종합적인 시장조사를 수행
(PEST, 3C, TAM/SAM/SOM, Porter 5 Forces, SWOT)

## Activated Agents
- **Primary**: MACRO-ANALYST, MARKET-ANALYST, COMPETITOR-INTEL
- **Support**: LEGAL-COMPLIANCE (규제 환경)

## Execution Steps

### Step 1: 거시환경 분석 (PEST + 3C)
```
MACRO-ANALYST 실행:
1. PEST 분석 (조지아)
   - Political: 정치 안정성, 외국인 투자 정책, EU 근접성
   - Economic: GDP, 소비력, 환율(GEL), 인플레이션
   - Social: 인구구조, 식문화, K-Culture 열풍
   - Technological: 배달앱 보급, 디지털 결제, IT 인프라
2. 3C 분석
   - Company: 자사 핵심역량 (생떡 제조 + IT 자동화)
   - Customer: 4개 타겟 페르소나 프로파일
   - Competitor: 경쟁 환경 개요
3. 기회-위협 매트릭스 도출
```

### Step 2: 시장 규모 조사
```
MARKET-ANALYST 실행:
1. 조지아 전체 외식시장 규모 (TAM)
2. 트빌리시 배달음식 시장 (SAM)
3. K-Food / 아시안 푸드 세그먼트 (SOM)
4. 시장 성장률 및 트렌드
```

### Step 3: 배달 플랫폼 분석
```
MARKET-ANALYST 실행:
1. Glovo Georgia 시장 현황
2. Wolt Georgia 시장 현황
3. 구역별 주문 밀도 분석
4. K-Food 검색 트렌드
```

### Step 4: 경쟁 환경 분석 (Porter 5 Forces)
```
COMPETITOR-INTEL 실행:
1. Porter's 5 Forces 체계적 분석
   - 기존 경쟁자 간 경쟁 강도
   - 신규 진입자 위협
   - 대체재 위협
   - 공급자 교섭력
   - 구매자 교섭력
2. 5 Forces 종합 매트릭스 (산업 매력도 점수)
3. 직접/간접/잠재 경쟁사 매핑
4. SWOT 크로스 분석 및 포지셔닝 맵
```

### Step 5: 규제 환경 조사
```
LEGAL-COMPLIANCE 실행:
1. 외국인 사업자 등록 절차
2. 식품 관련 인허가 요건
3. 세제 혜택 (Small Business Status)
```

## Output
- `output/research/pest-analysis.md` - PEST 분석
- `output/research/3c-analysis.md` - 3C 분석
- `output/research/market-size.md` - 시장규모 분석 (TAM/SAM/SOM)
- `output/research/delivery-platform.md` - 배달 플랫폼 분석
- `output/research/5forces-analysis.md` - Porter 5 Forces 분석
- `output/research/competition.md` - 경쟁 환경 분석
- `output/research/regulation.md` - 규제 환경 조사

## Usage
```
/bp-research                    # 전체 시장조사
/bp-research --pest             # PEST 분석만
/bp-research --3c               # 3C 분석만
/bp-research --market-size      # 시장규모만
/bp-research --5forces          # Porter 5 Forces만
/bp-research --competition      # 경쟁분석만
/bp-research --regulation       # 규제환경만
```
