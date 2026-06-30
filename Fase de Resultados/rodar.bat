@echo off
title FlowMind - Dashboard Fase 9

echo ============================================
echo           FlowMind - Fase 9
echo ============================================
echo.

:: Verifica se o Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado.
    echo Instale o Python e adicione-o ao PATH.
    pause
    exit /b
)

echo Instalando/verificando dependencias...
python -m pip install --upgrade pip
python -m pip install streamlit pandas duckdb plotly pyarrow

echo.
echo Preparando a base do dashboard...
python src\preparar_base_dashboard.py

if errorlevel 1 (
    echo.
    echo [ERRO] Falha ao preparar a base de dados.
    pause
    exit /b
)

echo.
echo Iniciando dashboard...
python -m streamlit run app\dashboard.py

pause