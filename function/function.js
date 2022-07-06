    async function copyPageUrl(data) {
        try {
            await navigator.clipboard.writeText(data);
            console.log('Page URL copied to clipboard');
        } catch (err) {
            console.error('Failed to copy: ', err);
        }
    }

    function encrypt_fun(key, data) {
        const result = encodemain(key, data);
        if (result.length >= 50) {
            copyPageUrl(result)
            $("#result").text('字符过长，已复制到剪切板');
        } else {
            $("#result").text('加密的结果是:' + result);
        }
    }

    function decrypt_fun(key, data) {
        const result = decodemain(key, data);
        if (result.length >= 50) {
            copyPageUrl(result)
            $("#result").text('字符过长，已复制到剪切板');
        } else {
            $("#result").text('解密的结果是:' + result);

        }
    }

    function fileread() {
        document.getElementById('encrypt').href = 'javascript:jiamifileImport()';
        document.getElementById('decrypt').href = 'javascript:jiemifileImport()';
        document.getElementById('ico_en').href = 'javascript:jiamifileImport()';
        document.getElementById('ico_de').href = 'javascript:jiemifileImport()';
        $("#files").click();
    }

    function downloadFile(fileName, content) {
        const a = document.createElement('a');
        const event = document.createEvent('MouseEvents');
        const blob = new Blob([content]);
        a.href = URL.createObjectURL(blob);
        a.download = fileName;
        event.initEvent('click', true, true);
        a.dispatchEvent(event);
    }


    function jiamifileImport() {
        //获取读取我文件的File对象
        const selectedFile = document.getElementById('files').files[0];
        const name = selectedFile.name;//读取选中文件的文件名
        const size = selectedFile.size;//读取选中文件的大小
        console.log("文件名:" + name + "大小:" + size);
        const reader = new FileReader();//这是核心,读取操作就是由它完成.
        reader.readAsDataURL(selectedFile);
        //reader.readAsText(selectedFile)
        reader.onload = function () {
            const result = encodemain(数据.key.value, this.result);
            document.getElementById("data").disabled = true;
            //当读取完成后回调这个函数,然后此时文件的内容存储到了result中,直接操作即可
            if (result === '密钥不能为空') {
                $("#result").text = '密钥不能为空'
            } else if (result === '密钥长度错误,请重新输入(密钥长度不能大于8)') {
                $("#result").text = '密钥长度错误,请重新输入(密钥长度不能大于8)'
            } else if (result === '输入的内容不是密文') {
                $("#result").text = '输入的内容不是密文'
            } else {
                downloadFile('result.data', result)
                $("#result").text = '已下载输出文件'
            }
        }
    }

    function jiemifileImport() {
        //获取读取我文件的File对象
        const selectedFile = document.getElementById('files').files[0];
        const name = selectedFile.name;//读取选中文件的文件名
        const size = selectedFile.size;//读取选中文件的大小
        console.log("文件名:" + name + "大小:" + size);
        const reader = new FileReader();//这是核心,读取操作就是由它完成.
        reader.readAsText(selectedFile)
        reader.onload = function () {
            //当读取完成后回调这个函数,然后此时文件的内容存储到了result中,直接操作即可
            const result = decodemain(数据.key.value, this.result);

            document.getElementById("data").disabled = true;
            if (result === '密钥不能为空') {
                $("#result").text = '密钥不能为空'
            } else if (result === '密钥长度错误,请重新输入(密钥长度不能大于8)') {
                $("#result").text = '密钥长度错误,请重新输入(密钥长度不能大于8)'
            } else if (result === '输入的内容不是密文') {
                $("#result").text = '输入的内容不是密文'
            } else {
                $("#download").href= result
                $("#download").click()
                $("#result").text = '已下载输出文件'

            }
        }
    }

    function oncancel_fun() {
        $("#data").text('已选择文件，若要清空文件，请刷新');
    }

