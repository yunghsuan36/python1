"""簡單的計算機模組，用來練習測試與 CI。"""


def add(a: float, b: float) -> float:
    """回傳 a + b。"""
    return a + b


def subtract(a: float, b: float) -> float:
    """回傳 a - b。"""
    return a - b


def multiply(a: float, b: float) -> float:
    """回傳 a * b。"""
    return a * b


def divide(a: float, b: float) -> float:
    """回傳 a / b；b 為 0 時丟出 ValueError。"""
    if b == 0:
        raise ValueError("除數不能是 0")
    return a / b


def average(numbers: list[float]) -> float:
    """回傳串列的平均值；空串列丟出 ValueError。"""
    if not numbers:
        raise ValueError("串列不能是空的")
    return sum(numbers) / len(numbers)
