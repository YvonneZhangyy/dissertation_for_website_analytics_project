# 修复Jupyter notebook中的问题

def fix_ipython_import():
    """修复IPython导入错误"""
    try:
        from IPython import get_ipython
        if get_ipython() is not None:
            get_ipython().run_line_magic('config', 'InteractiveShell.xmode = "Plain"')
    except ImportError:
        # IPython在非Jupyter环境中不可用，静默处理
        pass

def fix_callback_signature():
    """修复回调函数签名问题"""
    # 确保回调函数有正确的参数数量
    def update_event_impact_tab(active_tab):
        # 你的回调逻辑
        pass
    
    return update_event_impact_tab

# 推荐的修复代码
if __name__ == '__main__':
    # 修复IPython导入
    fix_ipython_import()
    
    # 修复回调函数
    update_event_impact_tab = fix_callback_signature()
    
    print("修复完成！") 