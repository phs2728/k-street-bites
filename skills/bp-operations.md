# Skill: /bp-operations (운영계획 — Value Chain, 기술성, HACCP)

## Purpose
떡 제조부터 배달까지의 전체 운영 프로세스 설계,
Value Chain 통합 분석, 기술성 분석 포함

## Activated Agents
- **Primary**: SCM-ENGINEER, QUALITY-CONTROL
- **Support**: WORKFLOW-AUTOMATION, MENU-RD, IT-INFRA

## Execution Steps

### Step 1: 제조 공정 설계
```
SCM-ENGINEER + MENU-RD 실행:
1. 떡 제조 프로세스 플로우
2. 메뉴별 조리 공정 (떡볶이, 순대 등)
3. 1일 최대 생산량 산출
4. SOP(표준운영절차) 작성
```

### Step 2: Value Chain 통합 분석
```
SCM-ENGINEER 실행:
1. 본원적 활동 (Primary Activities):
   - Inbound Logistics: 원재료 수입/조달
   - Operations: 떡 제조 공정
   - Outbound Logistics: 배달앱/B2B 배송
   - Marketing & Sales: 온/오프라인 판매
   - Service: 고객 CS, A/S
2. 지원 활동 (Support Activities):
   - 기술 개발, 인적 자원, 조달, 인프라
3. Make or Buy 분석: 내부 제조 vs 외부 조달 의사결정
4. 활동별 원가 배분 및 마진 분석
```

### Step 3: 기술성 분석
```
SCM-ENGINEER 실행:
1. 기술 적합성: 생떡 제조 기술 × 조지아 시장
2. 기술 차별성: 경쟁사 대비 기술 우위
3. 모방 난이도: 기술 장벽 평가
4. 기술 로드맵: 6개월/12개월/24개월 기술 발전 계획
```

### Step 4: 공급망 설계
```
SCM-ENGINEER 실행:
1. 원재료 조달 전략 (현지 vs 수입)
2. 공급업체 리스트 및 평가
3. 재고 관리 모델 (안전재고, 발주점)
4. 물류 최적화
```

### Step 5: 품질 관리 체계
```
QUALITY-CONTROL 실행:
1. HACCP 계획서
2. 품질 검사 체크리스트
3. 유통기한 관리 기준
4. 배달 품질 관리 기준
```

### Step 6: 자동화 및 IT 연동
```
WORKFLOW-AUTOMATION + IT-INFRA 실행:
1. 주문-생산-배송 자동화 설계
2. POS 시스템 연동
3. 재고 자동 관리 시스템
4. 운영 대시보드 설계
```

### Step 7: 설비 및 시설 계획
```
SCM-ENGINEER + IT-INFRA 실행:
1. 필요 설비 리스트 및 견적
2. 주방 레이아웃 설계
3. IT 인프라 구성
4. 설비 유지보수 계획
```

## Output
- `output/operations/manufacturing.md` - 제조 공정
- `output/operations/value-chain.md` - Value Chain 통합 분석
- `output/operations/technology-analysis.md` - 기술성 분석
- `output/operations/supply-chain.md` - 공급망
- `output/operations/quality-management.md` - 품질 관리 (HACCP)
- `output/operations/automation.md` - 자동화 설계
- `output/operations/equipment.md` - 설비 계획

## Usage
```
/bp-operations                  # 전체 운영계획
/bp-operations --manufacturing  # 제조공정만
/bp-operations --valuechain     # Value Chain만
/bp-operations --technology     # 기술성 분석만
/bp-operations --scm            # 공급망만
/bp-operations --quality        # 품질관리만
/bp-operations --automation     # 자동화만
```
