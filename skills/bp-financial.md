# Skill: /bp-financial (재무계획 및 투자분석)

## Purpose
추정 재무제표 3종(P&L, B/S, C/F) 작성, BEP 분석, ROI/NPV/IRR 투자 타당성 검증

## Activated Agents
- **Primary**: CFO-TAX
- **Support**: HR-TRAINING (인건비), B2B-SALES (B2B 매출),
  PERFORMANCE-MARKETING (마케팅 비용), SCM-ENGINEER (설비/원가),
  RISK-MANAGER (재무 리스크 시나리오)

## Execution Steps

### Step 1: 초기 투자 비용 (CAPEX)
```
CFO-TAX + SCM-ENGINEER 실행:
1. 설비 투자비 (떡 제조기, 주방장비)
2. 인테리어/시설비
3. IT 장비 (POS, 네트워크)
4. 법인설립/인허가 비용
5. 초기 원재료 구입
6. 운영 준비금 (3개월)
→ 총 초기 투자 금액 산출
```

### Step 2: 월간 운영 비용 (OPEX)
```
CFO-TAX + HR-TRAINING 실행:
1. 인건비 (대표 3,000 USD + 현지 직원)
2. 임대료
3. 원재료비 (매출 대비 %)
4. 배달앱 수수료
5. 마케팅비
6. 유틸리티/기타
→ 월간 고정비/변동비 산출
```

### Step 3: 매출 예측
```
CFO-TAX + MARKET-ANALYST + B2B-SALES 실행:
1. B2C 매출 예측 (배달앱 + 자체)
2. B2B 매출 예측 (납품)
3. 월별/연별 매출 성장 시나리오
   - Conservative (보수적): -20%
   - Base (기본): 0%
   - Optimistic (낙관적): +20%
```

### Step 4: 추정 재무제표 3종
```
CFO-TAX 실행:
1. 추정 손익계산서 (P&L) - 3년
   - 매출액, COGS, 매출총이익
   - SG&A, 영업이익, 세전/세후이익
2. 추정 재무상태표 (B/S) - 3년 + Year 0
   - 자산 (유동/비유동)
   - 부채 (유동/비유동)
   - 자본 (자본금/이익잉여금)
   - 주요 재무비율 (유동비율, 부채비율)
3. 추정 현금흐름표 (C/F) - 3년
   - 영업활동 현금흐름
   - 투자활동 현금흐름
   - 재무활동 현금흐름
   - 운전자본 관리 (CCC)
```

### Step 5: BEP 분석
```
CFO-TAX 실행:
1. 공헌이익률 (Contribution Margin Ratio)
2. 월 BEP 매출액 및 주문 건수
3. BEP 달성 예상 시점
```

### Step 6: 수익성 및 투자 타당성 분석
```
CFO-TAX + RISK-MANAGER 실행:
1. ROI (Return on Investment) - 연도별
2. NPV (Net Present Value) - 할인율 12%
3. IRR (Internal Rate of Return) - 목표 ≥25%
4. 투자금 회수기간 (Payback Period) - 목표 ≤24개월
5. 민감도 분석 (3 시나리오: 매출/원가 변동)
```

### Step 7: 투자 제안 및 자금 조달
```
CFO-TAX 실행:
1. 투자 라운드 구조 (Seed + 추가 Option)
2. 자금 조달 소스 (자기자본, 정부지원, 엔젤)
3. 투자자 수익 모델 (배당 정책, Exit 전략)
```

### Step 8: 세금 최적화
```
CFO-TAX + LEGAL-COMPLIANCE 실행:
1. Small Business Status 적용 시뮬레이션
2. VAT 등록 시점 판단
3. 세금 최적화 시나리오
```

## Output
- `output/financial/capex.md` - 초기 투자 계획
- `output/financial/opex.md` - 월간 운영 비용
- `output/financial/revenue-forecast.md` - 매출 예측
- `output/financial/pnl-3year.md` - 3년 추정 손익계산서 (P&L)
- `output/financial/balance-sheet.md` - 3년 추정 재무상태표 (B/S)
- `output/financial/cashflow.md` - 3년 추정 현금흐름표 (C/F)
- `output/financial/bep-analysis.md` - BEP 분석
- `output/financial/investment-feasibility.md` - ROI/NPV/IRR/민감도 분석
- `output/financial/investment-proposal.md` - 투자 제안서
- `output/financial/tax-optimization.md` - 세금 최적화

## Usage
```
/bp-financial                   # 전체 재무계획
/bp-financial --capex           # 초기 투자만
/bp-financial --pnl             # P&L만
/bp-financial --bs              # 재무상태표(B/S)만
/bp-financial --cf              # 현금흐름표(C/F)만
/bp-financial --bep             # BEP 분석만
/bp-financial --roi             # ROI/NPV/IRR만
/bp-financial --sensitivity     # 민감도 분석만
/bp-financial --investment      # 투자 제안서만
/bp-financial --tax             # 세금 최적화만
```
