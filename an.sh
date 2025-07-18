#!/bin/bash

echo "🚀 正在初始化虚拟环境并安装依赖..."

# 显示信息函数
info() { echo -e "\033[1;32m[INFO]\033[0m $1"; }
error() { echo -e "\033[1;31m[ERROR]\033[0m $1"; }

# 检查 Python3
if ! command -v python3 &> /dev/null; then
    error "未检测到 Python3，尝试自动安装..."

    if [ -f /etc/debian_version ]; then
        sudo apt update
        sudo apt install -y python3 python3-venv python3-pip
    elif [ -f /etc/redhat-release ]; then
        sudo yum install -y python3 python3-venv python3-pip || sudo dnf install -y python3 python3-pip
    else
        error "不支持的系统，请手动安装 Python3。"
        exit 1
    fi
fi

# 检查 venv 是否可用
if ! python3 -m venv --help > /dev/null 2>&1; then
    info "正在安装 python3-venv..."

    if [ -f /etc/debian_version ]; then
        sudo apt install -y python3-venv
    elif [ -f /etc/redhat-release ]; then
        sudo yum install -y python3-venv || sudo dnf install -y python3-venv
    else
        error "python3-venv 安装失败，请手动安装。"
        exit 1
    fi
fi

# 创建虚拟环境
if [ ! -d "venv" ]; then
    info "创建虚拟环境 venv..."
    python3 -m venv venv
else
    info "虚拟环境已存在，跳过创建。"
fi

# 激活虚拟环境
source venv/bin/activate

# 升级 pip
info "升级 pip..."
pip install --upgrade pip

# 写入固定的 requirements.txt（如不存在）
if [ ! -f "requirements.txt" ]; then
    info "生成默认 requirements.txt..."
    cat > requirements.txt <<EOF
setuptools
emoji
telethon
EOF
fi

# 安装依赖
info "根据 requirements.txt 安装依赖..."
pip install -r requirements.txt

info "✅ 安装完成！"

