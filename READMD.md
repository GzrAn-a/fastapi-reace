```
my_fastapi_project/
├── app/
│   ├── main.py              # 🚪 应用入口，只负责启动和注册路由
│   ├── core/                # ⚙️ 核心配置，如环境变量、安全设置
│   │   ├── config.py
│   │   └── security.py
│   ├── api/                 # 🛣️ API路由层，按业务模块或版本拆分
│   │   ├── v1/
│   │   │   ├── users.py     # 用户相关的路由 (类似 Controller)
│   │   │   └── items.py     # 物品相关的路由
│   │   └── routers.py       # 汇总所有路由
│   ├── models/              # 🗄️ 数据库模型层 (ORM)
│   │   ├── user.py
│   │   └── item.py
│   ├── schemas/             # 📝 数据校验层 (Pydantic)
│   │   ├── user.py
│   │   └── item.py
│   └── services/            # 💼 业务逻辑层 (真正的 Controller 逻辑)
│       ├── user_service.py
│       └── item_service.py
├── tests/                   # 🧪 测试用例
├── .env                     # 环境变量
├── requirements.txt         # 项目依赖
└── README.md
```

```shell
pip install -i requirements.txt
```

## app 是后端
## fastComd 是前端
