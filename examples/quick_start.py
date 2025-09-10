"""
Quick start example - README의 빠른 시작 코드
"""

import logging
import time
from bench_logging_handler import BenchHandler, ConsoleSink

def main():
    # 핸들러 설정
    handler = BenchHandler(sink=ConsoleSink())
    logging.getLogger().addHandler(handler)

    # 일반 로깅
    logging.info("애플리케이션이 시작되었습니다")

    # 벤치마킹
    bench_id = logging.benchstart("데이터베이스 쿼리")
    time.sleep(0.1)  # 실제 작업 시뮬레이션
    logging.benchend("쿼리 완료", bench_id)

if __name__ == "__main__":
    main()
