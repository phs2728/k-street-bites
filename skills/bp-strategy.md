# Skill: /bp-strategy (전략 수립 — 비전/미션/BMC/VRIO)

## Purpose
사업의 전략적 방향성, 비즈니스 모델, 핵심역량을 정의하고 경쟁 우위를 확립

## Activated Agents
- **Primary**: VISION-ARCHITECT, COMPETITOR-INTEL, IR-RELATIONS
- **Support**: MACRO-ANALYST, MARKET-ANALYST, MENU-RD

## Execution Steps

### Step 1: 5대 핵심질문 정의
```
VISION-ARCHITECT 실행:
1. WHY - 왜 이 사업을 하는가? (존재 이유)
2. WHAT - 무엇을 제공하는가? (핵심 가치)
3. HOW - 어떻게 구현하는가? (실행 방법)
4. WHO - 누구에게 제공하는가? (타겟 고객)
5. WHEN/WHERE - 언제, 어디서? (시장 진입)
```

### Step 2: 비전 및 미션 정의
```
VISION-ARCHITECT 실행:
1. 사업 비전 (3-5년 미래상)
2. 미션 스테이트먼트
3. 핵심 가치 (Core Values)
4. 경영 철학 및 차별화 원칙
```

### Step 3: Business Model Canvas (BMC)
```
VISION-ARCHITECT 실행:
1. BMC 9 Block 작성:
   - 고객 세그먼트 (← MACRO-ANALYST 페르소나)
   - 가치 제안 ("직접 뽑는 생떡" 체험)
   - 채널 (배달앱, 오프라인, SNS)
   - 고객 관계 (← CRM-SPECIALIST)
   - 수익원 (B2C + B2B)
   - 핵심 자원 (떡 제조 기술, K-Food 브랜드)
   - 핵심 활동 (← SCM-ENGINEER)
   - 핵심 파트너 (배달앱, 원재료 공급사)
   - 비용 구조 (← CFO-TAX)
```

### Step 4: VRIO 분석
```
VISION-ARCHITECT 실행:
핵심 자원별 VRIO 평가:
| 자원/역량 | V(가치) | R(희소성) | I(모방난이도) | O(조직적 지원) | 경쟁우위 |
- 생떡 제조 기술
- K-Food 브랜드
- IT 자동화 역량
- 조지아 시장 선점
- 현지화 메뉴 R&D
```

### Step 5: 경쟁 전략
```
COMPETITOR-INTEL 실행:
1. Porter's Five Forces 요약 (← /bp-research 결과)
2. Blue Ocean Strategy Canvas
3. 경쟁 포지셔닝 맵
4. USP 정의 ("직접 뽑는 떡" 차별화)
5. 진입 장벽 및 해자(Moat) 분석
```

### Step 6: 성장 로드맵
```
IR-RELATIONS + VISION-ARCHITECT 실행:
1. Phase 1 (0-6개월): 1호점 안정화, 브랜드 인지도
2. Phase 2 (6-12개월): 매출 극대화, B2B 시작
3. Phase 3 (12-24개월): 2호점 확장, 지역 확대
4. Phase 4 (24-36개월): B2B 확대 + 프랜차이즈 검토
```

## Output
- `output/strategy/5-key-questions.md` - 5대 핵심질문
- `output/strategy/vision-mission.md` - 비전/미션/핵심가치
- `output/strategy/business-model-canvas.md` - BMC (9 Block)
- `output/strategy/vrio-analysis.md` - VRIO 분석
- `output/strategy/competitive-strategy.md` - 경쟁 전략
- `output/strategy/growth-roadmap.md` - 성장 로드맵

## Usage
```
/bp-strategy                    # 전체 전략
/bp-strategy --vision           # 비전/미션 + 5대 핵심질문
/bp-strategy --bmc              # BMC만
/bp-strategy --vrio             # VRIO만
/bp-strategy --competition      # 경쟁전략만
/bp-strategy --roadmap          # 성장 로드맵만
```
