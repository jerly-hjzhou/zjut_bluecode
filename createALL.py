import webbrowser
#命名生成的html
GEN_HTML = "other.html" 
#打开文件，准备写入
f = open(GEN_HTML,'w', encoding="utf-8")

Message = """


<!DOCTYPE html><html><head>
    <title>申请人领取 - 学生校园通行码领取</title>
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="-1">
<meta name="keywords" content="InfoPlus">
<meta name="renderer" content="webkit">
<meta http-equiv="X-UA-Compatible" content="IE=Edge">
<meta itemscope="csrfToken" content="DtfxiNIfyug0mfGUN2hKrLz2mh4ArthK">
<meta name="theme-color" content="#039be5">
<!-- disable phone number link in mobile safari -->
<meta name="format-detection" content="telephone=no">
<link rel="icon" type="image/png" href="/infoplus/static/img/favicon.png">

<link href="/infoplus/static/css/infoplus.css?v=20200507-203528" rel="stylesheet">
    <link href="http://ehall.zjut.edu.cn/infoplus/static/themes/default/desktop/css/theme.css?v=20200507-203528" rel="stylesheet">
    <link href="http://ehall.zjut.edu.cn/infoplus/static/themes/default/mobile/css/theme.css?v=20200507-203528" rel="stylesheet">
    <link href="http://ehall.zjut.edu.cn/infoplus/static/themes/zjut/mobile/css/theme.css?v=20200507-203528" rel="stylesheet">
    <script type="text/javascript">
        var initGlobalVariable = function () {
            $$.PRINT = false;
            $$.VIEWS_ONLY = false;
            
        };

        var switchView = function () {
            $("#div_loader_progress").animate({height: "0", opacity: 0.5}, 200, function () {
                $("#div_loader").hide();
                $("#div_render_container").show();

                //触发全局表单可见事件，这里可以处理和表单中元素的高度、可见等相关的代码
                $$.visible();
            });
        };
    </script><style id="__WXWORK_INNER_SCROLLBAR_CSS">::-webkit-scrollbar { width: 12px !important; height: 12px !important; }::-webkit-scrollbar-track:vertical {  }::-webkit-scrollbar-thumb:vertical { background-color: rgba(136, 141, 152, 0.5) !important; border-radius: 10px !important; background-clip: content-box !important; border:2px solid transparent !important; } ::-webkit-scrollbar-track:horizontal {  }::-webkit-scrollbar-thumb:horizontal { background-color: rgba(136, 141, 152, 0.5) !important; border-radius: 10px !important; background-clip: content-box !important; border:2px solid transparent !important; } ::-webkit-resizer { display: none !important; }</style>
<style>[autoheight]{overflow: hidden;  box-sizing: border-box;}</style><style type="text/css"></style><script src="/infoplus/static/js/Release/render.min.js?v=20200507-203528"></script><script src="http://ehall.zjut.edu.cn/infoplus/static/themes/default/mobile/js/mobile.js?v=20200507-203528"></script><script src="http://ehall.zjut.edu.cn/infoplus/static/themes/zjut/mobile/js/render/mobile.js?v=20200507-203528"></script><style type="text/css" media="all" id="infoplus_view_7252_0_style"></style><link type="text/css" media="all" rel="stylesheet" id="infoplus_view_7252_0_cached_link" href="http://ehall.zjut.edu.cn/infoplus/form/css/1b17faf0245e53f306dbd0b9a6a25a08.css"></head>
<body>
<div id="help_content"></div>
<div id="div_loader" style="display: none;">
    <div id="div_loader_content">U
        <div id="div_loader_text">
            <span class="content">加载完成(100%)</span>
        </div>
        <div id="div_loader_progress" style="overflow: hidden; height: 0px; opacity: 0.5;">
            <div id="div_loader_progress_percent" style="right: 0%;"></div>
        </div>
    </div>
</div><div id="form_do_action_dialog" style="display:none;">
    <div id="form_do_action_message_description" style="display:none;"></div>
    <div id="form_do_action_show_remark" class="clearfix"></div>
    <div id="form_do_action_remark_div">
        <div id="form_do_action_remark_tip" style="margin-bottom:2px"></div>
        <textarea id="form_do_action_remark" rows="5"></textarea>
    </div>
    <div id="form_do_action_next_steps">
        <div id="form_do_action_show_next_steps" class="clearfix">
            <span class="form_do_action_info ui-icon ui-icon-info"></span>
            <span class="form_do_action_next_steps"></span>
        </div>
        <ul id="form_do_action_user_list"></ul>
    </div>
    <div style="height:10px"><a id="linkPrint" href="#" target="_blank"></a></div>
</div>


<div id="div_render_container" style="display: block;">
    <form id="renderForm">
        <div id="div_content" class="div_content">
            <div id="header_holder">
        <div id="title_holder" class="todo"><div id="title_icon" class="title_icon"><i class="i-icon-menu"></i></div><div id="title_content" style="max-width: 1763px;"><nobr>学生校园通行码领取:申请人领取</nobr></div><div><div id="title_description" style="">流水号:2313328,主管部门:党委学生工作部,研究生院</div><div id="title_description_short" style="display: none;">流水号:2313328</div></div></div>
        <!-- 1.form command bar -->
        <div id="command_holder">
            <div class="clear"></div>
            <div id="command_bar_title_icon" class="title_icon todo" style="display: none;"><i class="i-icon-menu"></i></div><ul id="form_command_bar"><li class="command_button"><a class="command_button_content" name="infoplus_action_9760_1" id="infoplus_action_9760_1"><nobr>通过</nobr></a><span class="alpha40 scroll_tip left" style="display: none;">点此区域按钮提交</span></li><li class="command_menu btn-group hide" id="command_menu"><a class="command_button_content dropdown-toggle command_button_all" href="#" data-toggle="dropdown">所有操作... <span class="caret"></span></a><ul class="dropdown-menu" id="command_menu_dropdown"><li><a title="" name="infoplus_command_menu_6878_1" id="infoplus_command_menu_6878_1">通过</a></li></ul><span class="alpha40 scroll_tip left" style="display: none;">点此区域按钮提交</span></li><li class="tool_button hide" style="display: none;"><a id="FormCommandGoTop" class="tool_button" href="#"><i class="i-icon-publish"></i></a></li></ul>
        </div>
    </div>
<div id="renderContent_holder"><div id="nav_menu" style="display: none;"><ul class="nav_menu_group"><li id="nav_menu_history"><span class="menu_icon menu_icon_history disabled"><i class="i-icon-history"></i></span><span class="menu_text disabled">历史</span></li><li id="nav_menu_save"><span class="menu_icon menu_icon_save"><i class="i-icon-save"></i></span><span class="menu_text">保存</span></li><li id="nav_menu_print"><span class="menu_icon menu_icon_print disabled"><i class="i-icon-print"></i></span><span class="menu_text">打印</span></li><li id="nav_menu_download"><span class="menu_icon menu_icon_download disabled"><i class="i-icon-cloud-download"></i></span><span class="menu_text">下载</span></li><li id="nav_menu_recover"><span class="menu_icon menu_icon_recover"><i class="i-icon-replay"></i></span><span class="menu_text">恢复提示</span></li><li id="nav_menu_instruction"><span class="menu_icon menu_icon_instruction disabled"><i class="i-icon-local-library"></i></span><span class="menu_text">填表说明</span></li></ul><ul class="nav_menu_group"><li class="nav_menu_line"></li></ul><ul class="nav_menu_group"><li id="nav_menu_help"><span class="menu_icon menu_icon_help"><i class="i-icon-help"></i></span><span class="menu_text">帮助</span></li></ul></div>
    <div id="form_milestone_holder" class="form_milestone_holder" style="display: none;visibility: hidden">
            <div class="form_milestone_holder_wrap_outer shadow round-corner">
                <div class="form_milestone_holder_wrap_inner">
                    <ul class="form_milestone_view"></ul>
                    <div class="clear"></div>
                </div>
            </div>
        </div>
    <!-- 2.the holder for form renderer -->
    <div id="render_holder">
        <div id="form_holder" style="display: block;"><div class="infoplus_view_wrap_outer"><div class="infoplus_view_wrap_inner"><div id="infoplus_view_7252_0" class="infoplus_view"><div align="center"><table style="BORDER-TOP-STYLE: none; WORD-WRAP: break-word; BORDER-LEFT-STYLE: none; WIDTH: 400px; BORDER-COLLAPSE: collapse; TABLE-LAYOUT: fixed; BORDER-BOTTOM-STYLE: none; BORDER-RIGHT-STYLE: none" class="xdFormLayout"><colgroup><col width="400" style="WIDTH: 400px"></colgroup><tbody><tr class="xdTitleRow"><td class="xdTitleCell" style="BORDER-TOP: #bfbfbf 1pt; BORDER-RIGHT: #bfbfbf 1pt; VERTICAL-ALIGN: middle; BORDER-BOTTOM: #808080 6pt; PADDING-BOTTOM: 0px; PADDING-TOP: 0px; PADDING-LEFT: 0px; BORDER-LEFT: #bfbfbf 1pt; PADDING-RIGHT: 0px"><h1 align="center"><div><img border="0" src="C:/Users/hp/Desktop/createBlue/firstP.jpg" style="HEIGHT: 133px; WIDTH: 400px"></div></h1></td></tr><tr class="xdTitleRow"><td class="xdTitleCell" style="BORDER-TOP: #808080 6pt; BORDER-RIGHT: #bfbfbf 1pt; VERTICAL-ALIGN: middle; BORDER-BOTTOM: #000000 1pt; PADDING-BOTTOM: 1px; PADDING-TOP: 1px; PADDING-LEFT: 1px; BORDER-LEFT: #bfbfbf 1pt; PADDING-RIGHT: 1px"><div align="center">Everyone is responsible for epidemic prevention on campus</div></td></tr><tr class="xdTitleRow"><td class="xdTitleCell" style="BORDER-TOP: #000000 1pt; BORDER-RIGHT: #bfbfbf 1pt; BORDER-BOTTOM: #000000 1pt; BORDER-LEFT: #bfbfbf 1pt"><div align="center"><div class="infoplus_labelControlContainer inline" id="label_210fe7f2-c637-4c87-b534-2fa0bacd122e_Container"><div style="FONT-SIZE: 16.5pt;font-family:'PingFang SC',微软雅黑; COLOR: #000000;" title="" class="infoplus_control infoplus_labelControl inline" id="label_210fe7f2-c637-4c87-b534-2fa0bacd122e">姓名</div><input type="hidden" id="V1_CTRL32" name="fieldXM" value="201806060729"></div><font style="FONT-SIZE: 16.5pt">&nbsp; 校园通行码&nbsp;&nbsp; </font>Campus Pass Code</div></td></tr><tr class="xdTitleRow"><td class="xdTitleCell" style="BORDER-TOP: #000000 1pt; BORDER-RIGHT: #808080 6pt; VERTICAL-ALIGN: middle; BORDER-BOTTOM: #808080 6pt; PADDING-BOTTOM: 10px; PADDING-TOP: 10px; PADDING-LEFT: 10px; BORDER-LEFT: #808080 6pt; PADDING-RIGHT: 10px"><font style="FONT-SIZE: 16.5pt"></font><div align="center"><div class="infoplus_labelControlContainer inline" id="label_31710deb-9103-4faa-826f-00b80fb04978_Container"><div style="FONT-SIZE: 16.5pt;font-family:'PingFang SC',微软雅黑; COLOR: #000000;" title="" class="infoplus_control infoplus_labelControl inline" id="label_31710deb-9103-4faa-826f-00b80fb04978">学院</div><input type="hidden" id="V1_CTRL34" name="fieldSZDW" value="21190"></div></div><div align="center"><div class="infoplus_labelControlContainer inline" id="label_f6924411-351f-4704-9a8a-9cfac1fa0b5c_Container"><div style="FONT-SIZE: 16.5pt;font-family:'PingFang SC',微软雅黑;" title="" class="infoplus_control infoplus_labelControl inline" id="label_f6924411-351f-4704-9a8a-9cfac1fa0b5c">身份</div><input type="hidden" id="V1_CTRL37" name="fieldSFZH" value="身份"></div><font style="FONT-SIZE: 16.5pt"></font></div></td></tr><tr class="xdTitleRow"><td class="xdTitleCell" style="BORDER-TOP: #808080 6pt; BORDER-RIGHT: #808080 6pt; VERTICAL-ALIGN: middle; BORDER-BOTTOM: #000000 1pt; BORDER-LEFT: #808080 6pt"><div align="left"><font style="FONT-SIZE: 16.5pt">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 生成时间</font><font size="3">&nbsp; </font>Generation time<font style="FONT-SIZE: 16.5pt">：</font></div><font style="FONT-SIZE: 16.5pt"><div align="center"><div class="infoplus_labelControlContainer" id="label_ffcd22d2-af27-445d-8fb8-972a0b64025d_Container"><div style="font-family: &quot;PingFang SC&quot;, 微软雅黑; min-height: 43px; line-height: 43px;" title="" class="infoplus_control infoplus_labelControl" id="label_ffcd22d2-af27-445d-8fb8-972a0b64025d">开始</div><input type="hidden" id="V1_CTRL35" name="fieldSCSJ" value="开始"></div></div></font><font style="FONT-SIZE: 16.5pt"></font><div align="left"><font style="FONT-SIZE: 16.5pt">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp; 到期时间</font>&nbsp; Expire Time<font style="FONT-SIZE: 16.5pt">：</font></div><font style="FONT-SIZE: 16.5pt"><div align="center"><div class="infoplus_labelControlContainer" id="label_65aa21e8-f8a7-4b7e-9bd7-342243ad45a0_Container"><div style="font-family: &quot;PingFang SC&quot;, 微软雅黑; min-height: 43px; line-height: 43px;" title="" class="infoplus_control infoplus_labelControl" id="label_65aa21e8-f8a7-4b7e-9bd7-342243ad45a0">结束</div><input type="hidden" id="V1_CTRL36" name="fieldDQSJ" value="2020-07-14 23:59:59"></div></div></font></td></tr><tr class="xdTableContentRow"><td class="xdTableContentCell" style="BORDER-TOP: #000000 1pt; BORDER-RIGHT: #808080 6pt; VERTICAL-ALIGN: middle; BORDER-BOTTOM: #bfbfbf 1pt; BORDER-LEFT: #808080 6pt"><div align="center"><div style="color: rgb(0, 112, 192);" title="" class="infoplus_control infoplus_pictureControl infoplus_readonly" id="picture_64a7e28c-6d4f-4f61-bb62-7ee7771422ec"><div class="displayDiv" style="width: 200px; height: 200px;"><a data-lightbox="525aec32-7d22-4864-b792-30dad861e3d4" href="http://ehall.zjut.edu.cn/file/4cc64fbe-5231-4255-83cd-b01a8b681dde"><img border="0" class="preview" style="display: none;"><img border="0" alt="XSXYTXM_qrcode39438.png" src="http://ehall.zjut.edu.cn/file/4cc64fbe-5231-4255-83cd-b01a8b681dde" style="margin-top: 0px; margin-left: 0px;" width="200" height="200"></a><div class="maskDiv" style="display: none; width: 200px; height: 200px;"></div><div title="删除" class="infoplus_pictureControl_delete"></div></div><div title="点击上传图片" class="uploadDiv" style="display: none; position: relative; overflow: hidden; direction: ltr; width: 200px; height: 200px;"><input qq-button-id="626f3808-6633-432a-a812-995e09a75888" title="" type="file" name="qqfile" style="position: absolute; right: 0px; top: 0px; font-family: Arial; font-size: 118px; margin: 0px; padding: 0px; cursor: pointer; opacity: 0; height: 200px;"></div><input type="hidden" id="V1_CTRL31" name="fieldQRCODE" value="4cc64fbe-5231-4255-83cd-b01a8b681dde"></div></div><div align="center">凭此码可在学校朝晖校区、屏峰校区、莫干山校区范围内配合有效证件通行，请主动出示，配合检查。</div><div align="center">This code can be used to pass with&nbsp;valid documents in the Zhaohui campus, Pingfeng campus and Moganshan campus. Please present it actively and cooperate with the inspection.<font face="Calibri"><font style="FONT-SIZE: 10.5pt"></font></font></div></td></tr></tbody></table></div><div align="center"></div></div></div></div><div id="variables_container"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_ACTION_ORGANIZE_Name" name="_VAR_ACTION_ORGANIZE_Name" value="学院"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_EXECUTE_ORGANIZES_Names" name="_VAR_EXECUTE_ORGANIZES_Names" value="学院"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_EXECUTE_INDEP_ORGANIZE_Name" name="_VAR_EXECUTE_INDEP_ORGANIZE_Name" value="学院"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_ACTION_ACCOUNT" name="_VAR_ACTION_ACCOUNT" value="201806060729"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_ACTION_INDEP_ORGANIZES_Codes" name="_VAR_ACTION_INDEP_ORGANIZES_Codes" value="21190"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_OWNER_ORGANIZES_Codes" name="_VAR_OWNER_ORGANIZES_Codes" value="21190"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_ADDR" name="_VAR_ADDR" value="115.200.35.234"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_URL_Attr" name="_VAR_URL_Attr" value="{&quot;membership&quot;:&quot;Wechat_Enterprise&quot;,&quot;showRemark&quot;:&quot;false&quot;}"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_ENTRY_NUMBER" name="_VAR_ENTRY_NUMBER" value="2313328"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_EXECUTE_INDEP_ORGANIZES_Names" name="_VAR_EXECUTE_INDEP_ORGANIZES_Names" value="学院"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_STEP_NUMBER" name="_VAR_STEP_NUMBER" value="2669977"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_POSITIONS" name="_VAR_POSITIONS" value="21190:4:201806060729
21190:6:201806060729
21190:2:201806060729"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_ACTION_REALNAME" name="_VAR_ACTION_REALNAME" value="姓名"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_OWNER_ORGANIZES_Names" name="_VAR_OWNER_ORGANIZES_Names" value="学院"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_URL" name="_VAR_URL" value="http://ehall.zjut.edu.cn/infoplus/form/2669977/render?membership=Wechat_Enterprise&amp;showRemark=false"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_ACTION_INDEP_ORGANIZES_Names" name="_VAR_ACTION_INDEP_ORGANIZES_Names" value="学院"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_EXECUTE_ORGANIZE_Name" name="_VAR_EXECUTE_ORGANIZE_Name" value="学院"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_EXECUTE_INDEP_ORGANIZES_Codes" name="_VAR_EXECUTE_INDEP_ORGANIZES_Codes" value="21190"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_RELEASE" name="_VAR_RELEASE" value="true"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_EXECUTE_POSITIONS" name="_VAR_EXECUTE_POSITIONS" value="21190:6:201806060729"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_OWNER_ACCOUNT" name="_VAR_OWNER_ACCOUNT" value="201806060729"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_NOW_MONTH" name="_VAR_NOW_MONTH" value="7"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_ACTION_USERCODES" name="_VAR_ACTION_USERCODES" value="201806060729"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_ACTION_ORGANIZES_Names" name="_VAR_ACTION_ORGANIZES_Names" value="学院"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_STEP_CODE" name="_VAR_STEP_CODE" value="step1"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_ACTION_ORGANIZE" name="_VAR_ACTION_ORGANIZE" value="21190"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_OWNER_USERCODES" name="_VAR_OWNER_USERCODES" value="201806060729"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_ACTION_ORGANIZES_Codes" name="_VAR_ACTION_ORGANIZES_Codes" value="21190"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_EXECUTE_ORGANIZE" name="_VAR_EXECUTE_ORGANIZE" value="21190"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_EXECUTE_INDEP_ORGANIZE" name="_VAR_EXECUTE_INDEP_ORGANIZE" value="21190"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_EXECUTE_ORGANIZES_Codes" name="_VAR_EXECUTE_ORGANIZES_Codes" value="21190"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_NOW_DAY" name="_VAR_NOW_DAY" value="14"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_ACTION_INDEP_ORGANIZE" name="_VAR_ACTION_INDEP_ORGANIZE" value="21190"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_OWNER_REALNAME" name="_VAR_OWNER_REALNAME" value="姓名"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_NOW_YEAR" name="_VAR_NOW_YEAR" value="2020"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_ACTION_INDEP_ORGANIZE_Name" name="_VAR_ACTION_INDEP_ORGANIZE_Name" value="学院"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_NOW" name="_VAR_NOW" value="1594741286"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_ENTRY_NAME" name="_VAR_ENTRY_NAME" value="学生校园通行码领取_姓名"><input type="hidden" class="infoplus_control infoplus_hiddenControl infoplus_var" id="_VAR_ENTRY_TAGS" name="_VAR_ENTRY_TAGS" value="学生事务,学生,移动端"></div></div>
    </div>
    <!-- 5.the holder for form remark renderer -->
        <div id="form_remark_holder" class="form_remark_holder shadow round-corner" align="center" style="display: none; width: 420px;"></div>
    </div>

</div>
    </form>
<div id="master_footer"><div id="div_footer_copy_containers"><div style="height:1px;background-color:#999999"></div><div style="height:1px;background-color:#FFFFFF"></div><div id="div_footer_copy_content">版权所有 © 浙江工业大学</div></div></div></div>
<script language="JavaScript">
    //如果发现在iframe里面就加载iframe.css，主要解决jquery的offset计算错误的问题
    if (self !== top) {
        var link = document.createElement('link');
        link.setAttribute("rel", "stylesheet");
        link.setAttribute("type", "text/css");
        link.setAttribute("href", "/infoplus/static/css/iframe.css?v=20200507-203528");
        document.getElementsByTagName("head")[0].appendChild(link);
    }
</script>

<script type="text/javascript" src="/infoplus/static/js/lib/lib.js?v=20200507-203528"></script>
<script type="text/javascript" src="/infoplus/static/js/lang_zh.js?v=20200507-203528"></script>
    <script type="text/javascript">
    var googleAnalysis = function () {
        
    };


    
    var entrusts = {"entrustee":{"account":"201806060729","email":"","phone":"","title":"","memberships":{"f0ae6c10-a924-4150-bb9d-1bea120b31be":{"id":"201806060729","memberId":"201806060729","membershipId":"f0ae6c10-a924-4150-bb9d-1bea120b31be","provider":"Wechat_Enterprise"}},"id":"7b270ac0-a585-11e8-b601-0050569b9b9b","name":"姓名"},"entrusted":false};
    


    var progressFlag = null;

    //判断是否是移动端APP请求
    var isMobileApp = function () {
        return navigator.userAgent.match(/TaskCenterApp/);
    };

    var progress = function (content, percent, targetPercent, waitMillisecond) {

        if (isMobileApp()) {
            return;
        }

        var showPercent = function (p, waitingTimes) {
            $("#div_loader_progress_percent").css("right", (100 - p) + "%");
            var $loaderTextDiv = $("#div_loader_text");
            var $loaderText = $loaderTextDiv.children(".content");
            $loaderTextDiv.children(".waiting").remove();
            $loaderText.text(content + "(" + p + "%)");

            if (waitingTimes != null) {
                //超过3秒再显示请耐心等待
                var waitingString = waitingTimes > 60 ? '请耐心等待' : '';
                for (var i = 0, len = Math.floor(waitingTimes / 3) % 6; i < len; i++) {
                    waitingString += '.';
                }
                if ($loaderTextDiv.children(".waiting").length == 0) {
                    var span = document.createElement("span");
                    $(span).addClass("waiting").text(waitingString);
                    $loaderTextDiv.append(span);
                } else {
                    $loaderTextDiv.children(".waiting").text(waitingString);
                }
            }

            var $loader = $("#div_loader");
            if (!$loader.is(":visible")) {
                $loader.show();
            }

        };

        if (progressFlag != null) {
            clearInterval(progressFlag);
        }

        showPercent(percent);

        if (targetPercent != null) {
            var frames = 20,
                currentPercent = percent,
                percentStep = (targetPercent - percent) / frames,
                waitingTimes = 0;
            var wait = waitMillisecond == null ? 1000 : waitMillisecond;

            progressFlag = setInterval(function () {
                currentPercent += percentStep;
                currentPercent = Math.floor(currentPercent);
                if (currentPercent > targetPercent) {
                    waitingTimes++;
                    //showPercent(targetPercent, waitingTimes);
                    showPercent(targetPercent);
                } else {
                    showPercent(currentPercent);
                }

            }, wait / frames)
        }
    };

    var loadFormError = function () {
        if (progressFlag != null) {
            clearInterval(progressFlag);
        }

        var title = "加载流程失败",
            $loaderTextDiv = $("#div_loader_text"),
            $loaderText = $loaderTextDiv.children(".content");
        $loaderTextDiv.children(".waiting").remove();
        $loaderText.text(title);
        $("#div_loader_progress_percent").css("right", "0").css("background-color", "red");
    };

    var workflowId, formStepId, instanceId;
    
    formStepId = 2669977;
    instanceId = "";
    workflowId = null;
    

    var instanceView = false;
    
    var adminView = false;
    


    var transformer = null;


    var setInitRemarkWidth = function () {
        //非移动版初始时候设置历史宽度）
        if (!$$.MOBILE) {
            var flag = setInterval(function () {
                var width = $("#render_holder")[0].clientWidth;
                if (width > 0) {
                    //不设置宽度的话，如果历史备注比较长会撑大整个DIV
                    //如果全部的view都是自动宽度，那么remarkholder宽度设成100%，不需要这里再设置了
                    if (!$$.params.allAutoWidth) {
                        $$.params.holder.remark.css("width", width + "px");
                    } else {
                        $$.params.holder.remark.css("width", "100%");
                    }
                    clearInterval(flag);
                    $$.params.currentWidth = width;
                    $$.resize(width);
                }
            }, 100);

        }
    };

    var startLoad = function () {

        transformer.load().done(function () {

            setInitRemarkWidth();
            transformer.registerGlobalEvents();

            //渲染完毕
            progress($$.lt("load.finish"), 100);

            //如果是被嵌入在移动app中，那么调用webViewInterface函数
            if (isMobileApp()) {
                if (window['webViewInterface'] !== undefined && window['webViewInterface']['loaded'] !== undefined) {
                    try {
                        webViewInterface.loaded();
                    } catch (ignore) {
                    }
                }
            }

            setTimeout(switchView, 0);

            

            //触发ready事件
            $$.ready();

            googleAnalysis();

        });
    };

    var startPreview = function () {
        var previewConfig = {
            app: {
                
                iconUrl: "/infoplus/static/img/default_workflow_icon.png",
                
                iconPalette: "",
                name: "",
                department: "",
                contact: "",
                rating:0,
                rated:0
            },
            release: "",
            idc: "",
            
            clear:false,
            
            startable: false
        };

        transformer.preview(previewConfig).done(function () {
            //渲染完毕
            /*
            if (!$$.MOBILE) {
                setInitRemarkWidth();
            } else {
                $$.resize($(window).width());
            }
            */
            setInitRemarkWidth();
            transformer.registerGlobalEvents();


            //如果是被嵌入在移动app中，那么调用webViewInterface函数
            if (isMobileApp()) {
                if (window['webViewInterface'] !== undefined && window['webViewInterface']['loaded'] !== undefined) {
                    try {
                        webViewInterface.loaded();
                    } catch (ignore) {
                    }
                }
            }

            setTimeout(switchView, 0);

            //触发ready事件
            $$.ready();

            googleAnalysis();
        });
    };

    var loadTransformer = function () {

        initGlobalVariable();

        if ($$.MOBILE) {
            var width = $(window).width();
            if (width > 0) {
                $("#form_remark_holder").css("width", width + "px");
                $("#form_holder").css("width", width + "px");
            }
        }

        var $commandHolder = $("#command_holder");

        transformer = new InfoPlus.Transformer({
            formStepId: formStepId,
            instanceId: instanceId,
            workflowId: workflowId,
            instanceView: instanceView,
            adminView: adminView,
            
            userId: "7b270ac0-a585-11e8-b601-0050569b9b9b",
            account: "201806060729",
            tenantId: "5f206195-366b-444f-86e3-a23d4c350c18",
            tenantDomain: "zjut.edu.cn",
            synthesizeEmail:false,
            tenantTimeZoneOffset: 28800,
            tenantReadOnlyStyle: "Label",
            lang: "zh",
            
            entrusts: entrusts,
            
            url_print: "/infoplus/form/2669977/print",
            url_download_pdf: "/infoplus/form/2669977/export.pdf",
            url_download_word: "/infoplus/form/2669977/export.docx",
            
            url_reLogin: "/infoplus/form/reLogin",
            lib_ckeditor: "/infoplus/static/js/lib/ck/ckeditor.js",

            interface_render: "/infoplus/interface/render",
            interface_preview: "/infoplus/interface/preview",
            interface_start: "/infoplus/interface/start",
            interface_list_remarks: "/infoplus/interface/instance/{id}/progress",
            interface_list_next_steps: "/infoplus/interface/listNextStepsUsers",
            interface_do_action: "/infoplus/interface/doAction",
            interface_withdraw: "/infoplus/interface/withdraw",
            interface_kill: "/infoplus/interface/kill",
            interface_delete_attachment: "/infoplus/interface/deleteAttachment",
            interface_save: "/infoplus/interface/save",
            interface_fieldChange: "/infoplus/interface/fieldChanging",
            interface_buttonClick: "/infoplus/interface/fieldChanging",
            interface_suggest: "/infoplus/interface/suggest",
            interface_suggestInitialize: "/infoplus/interface/suggestInitialize",
            interface_thing: "/infoplus/interface/thing",
            interface_printInvoice: "",
            
            interface_entrust: "/infoplus/interface/entrust",
            interface_users: "/infoplus/interface/suggest",
            interface_compare: "/infoplus/interface/data",
            interface_ckUploadImage: "/infoplus/interface/ckUploadImage",
            interface_changePriority: "/infoplus/interface/priority",
            interface_attachment: "/infoplus/interface/attachment",
            interface_attachmentToken: "/infoplus/interface/attachmentToken",
            interface_graphql: "/infoplus/interface/graphql",
            
            copyright: "版权所有 © 浙江工业大学",
            
            base_url: '/infoplus/'

        });

        //transformer.registerGlobalEvents();


        //参数上要求弹出委托对话框或者不存在委托(调试)人情况下，显示委托选人对话框
        if (transformer.entrust === "true" && !(transformer.entrusts != null && transformer.entrusts.entruster != null)) {
            $IU.chooseEntrust(transformer.entrusts, null, ($$.PREVIEW ? startPreview : startLoad), transformer.interface_entrust);
        } else {
            if ($$.PREVIEW) {
                startPreview();
            } else {
                startLoad();
            }
        }

    };

    //var __file__ = null;
    var loadScriptCallback = function () {
        loadTransformer();
    };

    

    $(document).ready(function () {
        
        if (checkBrowser()) {
            
            if (entrusts.entruster == null) {
                progress(InfoPlus.Language.load.loadPage, 0, 20, 1000);
            }
            
            loadScript();
        }
        
    });

</script>

<script type="text/javascript">
    var loadScript = function () {

        var jsFiles;
        
        jsFiles = [
            [
                "/infoplus/static/js/Release/render.min.js?v=20200507-203528"
            ]
        ];
        
        jsFiles.push([
            "http://ehall.zjut.edu.cn/infoplus/static/themes/default/mobile/js/mobile.js?v=20200507-203528",
        ]);
        
        jsFiles.push([
            "http://ehall.zjut.edu.cn/infoplus/static/themes/zjut/mobile/js/render/mobile.js?v=20200507-203528",
        ]);
        
        loadScriptSeq(jsFiles, loadScriptCallback);
        


    };
</script>
<div id="div_invoice"></div>
<iframe id="alive" src="/infoplus/alive" style="display: none; border:0">unsupported.</iframe>



</body></html>


"""
import time
newName=input("your name:")
newPartment=input("input your department:")
newID=input("input your ID:")
newTime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
newMessage1 = Message.replace("姓名",newName)
newMessage2 = newMessage1.replace("学院",newPartment)
newMessage3 = newMessage2.replace("开始",newTime+" 00:00:00")
newMessage4 = newMessage3.replace("结束",newTime+" 23:59:59")
newMessage5 = newMessage4.replace("身份",newID)
#写入文件
f.write(newMessage5) 
#关闭文件
f.close()
 
#运行完自动在网页中显示
webbrowser.open(GEN_HTML,new = 1) 