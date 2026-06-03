# 示例：使用 Python 代码审查模板

## 场景描述
对一段 FastAPI 用户注册接口代码进行安全和质量审查。

## 变量填充

| 变量 | 填充值 |
|------|--------|
| CODE_SNIPPET | （见下方代码） |
| PYTHON_VERSION | 3.11 |
| FRAMEWORK | FastAPI 0.104 + SQLAlchemy 2.0 |
| CODE_CONTEXT | 用户服务模块，处理注册/登录/密码重置 |

## 待审查代码

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate
from app.database import get_db
import hashlib

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    # 检查用户是否存在
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # 创建用户
    hashed_password = hashlib.md5(user.password.encode()).hexdigest()
    new_user = User(
        email=user.email,
        username=user.username,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id": new_user.id, "email": new_user.email}
```

## 生成的完整 Prompt

你是一位资深 Python 技术专家，拥有 10 年以上的 Python 开发经验和安全审计背景。

请对以下 Python 代码进行全面的 Code Review：

**Python 版本**：3.11
**框架**：FastAPI 0.104 + SQLAlchemy 2.0
**代码上下文**：用户服务模块，处理注册/登录/密码重置

**待审查代码**：
（代码如上）

**审查维度（按优先级）**：
- P0：安全漏洞（SQL 注入、命令注入、反序列化）
- P1：逻辑错误、异常处理缺陷、资源泄漏
- P2：性能问题（N+1 查询、GIL 阻塞、内存）
- P3：PEP8 合规、类型注解完整性
- P4：测试覆盖、文档完善度

**输出格式**：按优先级排列问题清单，每个问题包含：
1. 严重级别（P0-P4）
2. 问题所在行号
3. 问题描述
4. 修复建议（含代码示例）

## 预期审查结果示例

| 级别 | 行号 | 问题 | 修复建议 |
|------|------|------|---------|
| P0 | 18 | 使用 MD5 哈希密码，极易被彩虹表破解 | 改用 bcrypt 或 argon2 |
| P1 | 21-23 | 缺少 try/except，db.commit() 失败时无回滚 | 添加异常处理和 db.rollback() |
| P2 | 13 | 未对 email 字段添加索引查询条件 | 确认数据库 email 字段已建索引 |
