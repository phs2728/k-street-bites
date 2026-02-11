#!/usr/bin/env python3
"""
K-Street Bites 사업계획서 PDF 생성기
=====================================
HTML 인포그래픽을 PDF로 변환합니다.

사용법:
    python generate_pdf.py

필요 패키지:
    pip install playwright
    playwright install chromium
"""

import asyncio
import os
import sys
from pathlib import Path
from datetime import datetime

# 색상 출력용
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header():
    """헤더 출력"""
    print(f"""
{Colors.CYAN}{'='*60}
   K-Street Bites 사업계획서 PDF 생성기
   Business As Mission - 투자자용 문서
{'='*60}{Colors.END}
""")

def print_step(step, message):
    """단계별 메시지 출력"""
    print(f"{Colors.GREEN}[{step}]{Colors.END} {message}")

def print_error(message):
    """에러 메시지 출력"""
    print(f"{Colors.FAIL}[ERROR]{Colors.END} {message}")

def print_success(message):
    """성공 메시지 출력"""
    print(f"{Colors.GREEN}[SUCCESS]{Colors.END} {message}")

async def generate_pdf_with_playwright():
    """Playwright를 사용하여 PDF 생성"""
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print_error("playwright 패키지가 설치되지 않았습니다.")
        print(f"\n{Colors.CYAN}설치 방법:{Colors.END}")
        print("  pip install playwright")
        print("  playwright install chromium")
        return False
    
    # 경로 설정
    script_dir = Path(__file__).parent
    html_file = script_dir / "investor-pitch-summary.html"
    pdf_file = script_dir / f"K-Street-Bites-투자제안서-{datetime.now().strftime('%Y%m%d')}.pdf"
    
    if not html_file.exists():
        print_error(f"HTML 파일을 찾을 수 없습니다: {html_file}")
        return False
    
    print_step("1/4", f"HTML 파일 로드: {html_file.name}")
    
    async with async_playwright() as p:
        print_step("2/4", "Chromium 브라우저 시작...")
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # HTML 파일 로드
        await page.goto(f"file://{html_file.absolute()}")
        
        print_step("3/4", "차트 렌더링 대기...")
        # Chart.js 렌더링 대기
        await page.wait_for_timeout(2000)
        
        print_step("4/4", "PDF 생성 중...")
        await page.pdf(
            path=str(pdf_file),
            format='A4',
            print_background=True,
            margin={
                'top': '0mm',
                'right': '0mm',
                'bottom': '0mm',
                'left': '0mm'
            }
        )
        
        await browser.close()
    
    print_success(f"PDF 생성 완료: {pdf_file.name}")
    print(f"\n{Colors.CYAN}파일 위치:{Colors.END} {pdf_file}")
    return True

def generate_pdf_alternative():
    """대체 방법: 브라우저에서 직접 PDF 저장 안내"""
    script_dir = Path(__file__).parent
    html_file = script_dir / "investor-pitch-summary.html"
    
    print(f"""
{Colors.WARNING}{'='*60}
   대체 방법: 브라우저에서 PDF 저장
{'='*60}{Colors.END}

Playwright가 설치되지 않은 경우, 다음 방법을 사용하세요:

{Colors.CYAN}방법 1: Chrome/Edge 브라우저{Colors.END}
  1. 아래 파일을 브라우저에서 엽니다:
     {Colors.GREEN}{html_file}{Colors.END}
  
  2. Ctrl+P (인쇄) 누르기
  
  3. "대상"에서 "PDF로 저장" 선택
  
  4. "저장" 버튼 클릭

{Colors.CYAN}방법 2: VS Code Live Server{Colors.END}
  1. VS Code에서 HTML 파일 열기
  2. 우클릭 → "Open with Live Server"
  3. 브라우저에서 Ctrl+P → PDF로 저장

{Colors.CYAN}방법 3: Playwright 설치{Colors.END}
  pip install playwright
  playwright install chromium
  python generate_pdf.py
""")

def check_dependencies():
    """의존성 확인"""
    try:
        import playwright
        return True
    except ImportError:
        return False

async def main():
    """메인 함수"""
    print_header()
    
    # 현재 디렉토리 확인
    script_dir = Path(__file__).parent
    html_file = script_dir / "investor-pitch-summary.html"
    
    if not html_file.exists():
        print_error(f"HTML 파일이 없습니다. 먼저 investor-pitch-summary.html을 생성하세요.")
        return
    
    # Playwright 확인
    if check_dependencies():
        success = await generate_pdf_with_playwright()
        if not success:
            generate_pdf_alternative()
    else:
        generate_pdf_alternative()
    
    # 추가 파일 정보
    print(f"""
{Colors.CYAN}{'='*60}
   생성된 파일 목록
{'='*60}{Colors.END}
""")
    
    output_files = [
        ("investor-pitch-summary.html", "투자자용 인포그래픽 (4페이지)"),
        ("K-Street-Bites-사업계획서.md", "전체 사업계획서 (Markdown)"),
        ("generate_pdf.py", "PDF 생성 스크립트"),
        ("generate_docx.py", "Word 문서 생성 스크립트"),
    ]
    
    for filename, desc in output_files:
        filepath = script_dir / filename
        status = f"{Colors.GREEN}✓{Colors.END}" if filepath.exists() else f"{Colors.FAIL}✗{Colors.END}"
        print(f"  {status} {filename}: {desc}")

if __name__ == "__main__":
    asyncio.run(main())
