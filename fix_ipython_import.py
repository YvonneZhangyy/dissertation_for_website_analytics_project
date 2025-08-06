# 修复IPython导入错误的解决方案

# 方案1: 使用try-except包装IPython导入
def fix_ipython_import():
    """
    修复IPython导入错误的函数
    在非Jupyter环境中安全地处理IPython导入
    """
    try:
        from IPython import get_ipython
        if get_ipython() is not None:
            get_ipython().run_line_magic('config', 'InteractiveShell.xmode = "Plain"')
    except ImportError:
        # IPython在非Jupyter环境中不可用，静默处理
        pass

# 方案2: 完全移除IPython依赖
def remove_ipython_dependency():
    """
    完全移除IPython依赖的替代方案
    """
    # 直接设置配置，不依赖IPython
    import sys
    if 'ipykernel' in sys.modules:
        # 在Jupyter环境中运行
        print("Running in Jupyter environment")
    else:
        # 在非Jupyter环境中运行
        print("Running in non-Jupyter environment")

# 推荐的修复代码
if __name__ == '__main__':
    # 使用方案1修复IPython导入
    fix_ipython_import()
    
    # 或者使用方案2完全移除依赖
    # remove_ipython_dependency() 