from notification.model import Message

messages = [
    {
        "title": "이번 주 회의 건 수",
        "content": "이번 주 {{task_count}}개의 회의가 예정되어 있어요."
    },
    {
        "title": "새로운 회의",
        "content": "새로운 회의가 있습니다.\n 담당자: {{owner}} | 시간: {{}}"
    },
    {
        "title": "회의 시작 10분 전",
        "content": "{{meeting_name}} 회의가 10분 뒤에 {{location}}에서 실행돼요."
    },
]
