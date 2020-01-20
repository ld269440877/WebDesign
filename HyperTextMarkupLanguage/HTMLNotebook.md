
# HTMLNotebook

> 参考  
> [每个人都应该知道的基本Web术语](https://badhtml.com/basic-concepts/)  
> [如何有效快速的学习HTML/CSS/JS](https://www.zhihu.com/question/23714828)  
> [HTML Cheat Sheet 📃 - The best interactive cheat sheet](https://htmlcheatsheet.com/)  
> [Online WYSIWYG HTML Editor | 𝗣𝗿𝗼𝗳𝗲𝘀𝘀𝗶𝗼𝗻𝗮𝗹 𝗧𝗼𝗼𝗹𝗸𝗶𝘁](https://htmlg.com/html-editor/)  
> [在线所见即所得HTML编辑器| 𝗧𝗼𝗼𝗹𝗸𝗶𝘁](https://htmlg.com/html-editor/)  
> [HTML 基础教程](https://www.w3school.com.cn/html/html_jianjie.asp)
> [HTML 参考手册](https://www.w3school.com.cn/tags/html_ref_byfunc.asp)  
> [HTML在线测试-W3School TIY Editor](https://www.w3school.com.cn/tiy/t.asp?f=html_headers)  
> [在Markdown中嵌入youtube视频的写法](https://gist.github.com/aoxu/7783280#file-youtube-md)  
> [HTML 实体字符参考手册](https://www.w3school.com.cn/tags/html_ref_entities.html)  
> [W3C-World Wide Web Consortium 简介](https://www.w3school.com.cn/w3c/w3c_intro.asp)  

> [网页浏览大图片速度测试 - Website Performance and Optimization Test](https://www.webpagetest.org/)


html css 和js关系
1. html是一个网页的主题，是由多个元素组合成的，但是这写元素保留的是基本默认属性，
2. css就是这个网页的样式，css定义了元素的属性，
3. js是通过jacascript语言，实现在一个页面上展现不同的css样式。
> 它们的关系通俗讲就是 html是一个赤裸裸的人，css是人的衣服，js作用是让人动起来。

javascript是编程语言，html和css不是编程语言

javascript是脚本语言，它是连接前台（html）和后台服务器的桥梁，它是操纵html的能手，本文用js代替javascript进行说明。

平时听到原生js，js库，js框架，js插件等等，下面简单说明一下。
- 原生js，是指最基础的js，没有封装过，但因为各浏览器对js的支持不同，就导致用基础的js编程需要为不同的浏览器写兼容代码。
- Js库，js框架，是指集成一系列dom操作，API封装，界面UI封装的的库类，常见的有jQuery，extjs等等，这方面的定义比较难区分，暂不误导大家
- Js插件，就是集成了帮助程序员轻松完成功能的程序。Js插件用得比较多，网页制作上随处可见。如图片轮换功能，导航制作，上传图片等等。


<figure>
   <center>
   <a href="http://www.tablesgenerator.com/html_tables">
   <img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116225405.png" alt="20200117171735"  title="在线表格生成器图片链接" width="600" height="" />
   <figcaption>Figure - 在线表格生成器图片链接</figcaption>
   </a>
   </center>
</figure>

---

# HTML 简介

## 实例

```html
<html>
<body>

<h1>我的第一个标题</h1>

<p>我的第一个段落。</p>

</body>
</html>
```
## 什么是 HTML？

HTML 是用来<font color=red>描述网页的一种语言</font>。

- HTML 指的是超文本标记语言 (Hyper Text Markup Language)
- HTML <font color=orange>不是一种编程语言</font>，而是一种标记语言 (markup language)
- 标记语言是一套标记标签 (markup tag)
- HTML 使用标记标签来描述网页

## HTML 标签

HTML 标记标签通常被称为 HTML 标签 (HTML tag)。

HTML 标签是由尖括号包围的关键词，比如 `<html>`
HTML 标签通常是成对出现的，比如 `<b>` 和 `</b>`
标签对中的第一个标签是开始标签，第二个标签是结束标签
开始和结束标签也被称为开放标签和闭合标签

## HTML 文档 = 网页

- HTML 文档描述网页
- HTML 文档包含 HTML 标签和纯文本
- HTML 文档也被称为网页

Web 浏览器的作用是读取 HTML 文档，并以网页的形式显示出它们。浏览器不会显示 HTML 标签，而是使用标签来解释页面的内容：
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/web浏览器读取html文档.png" alt="web浏览器读取html文档"  title="web浏览器读取html文档" width="600" height=""></center>

## 例子解释

`<html>` 与 `</html>` 之间的文本描述网页
`<body>` 与 `</body>` 之间的文本是可见的页面内容
`<h1>` 与 `</h1>` 之间的文本被显示为标题
`<p>` 与 `</p>` 之间的文本被显示为段落

# 基本的 HTML 标签 - 四个实例

> 提示：学习 HTML 最好的方式就是边学边做实验。

## HTML 标题
HTML 标题（Heading）是通过 `<h1> - <h6>` 等标签进行定义的。

实例
```html
<h1>This is a heading</h1>
<h2>This is a heading</h2>
<h3>This is a heading</h3>
```

## HTML 段落
HTML 段落是通过 <p> 标签进行定义的。

实例
```html
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/html段落标签p.png" alt="html段落标签p"  title="html段落标签p" width="600" height=""></center>

## HTML 链接

HTML 链接是通过 `<a>` 标签进行定义的。

实例
```html
<a href="http://www.w3school.com.cn">This is a link</a>
<!-- 注释：在 href 属性中指定链接的地址。 -->
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/HTML链接标签a.png" alt="HTML链接标签a"  title="HTML链接标签a" width="600" height=""></center>

## HTML 图像
HTML 图像是通过 `<img>` 标签进行定义的。

实例
```html
<img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/HTML图像标签img.png" width="104" height="142" />
<!-- 注释：图像的名称和尺寸是以属性的形式提供的。 -->
```

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/html图像标签img.png" alt="HTML图像标签img"  title="HTML图像标签img" width="600" height="" /></center>

# HTML 元素

HTML 文档是由 HTML 元素定义的。

<font color=red>HTML 元素</font>
    : 从开始标签（start tag）到结束标签（end tag）的所有代码。

| 开始标签                  | 元素内容            | 结束标签 |
| ------------------------- | ------------------- | -------- |
| `<p>`                     | This is a paragraph | `	</p>`  |
| `<a href="default.htm" >` | This is a link      | `</a>`   |
| `<br />`                  |                     |          |

> 注释：开始标签常被称为开放标签（opening tag），结束标签常称为闭合标签（closing tag）。

## HTML 元素语法

- HTML 元素以开始标签起始
- HTML 元素以结束标签终止
- **元素的内容**是开始标签与结束标签之间的内容
- 某些 HTML 元素具有空内容（empty content）
- **空元素**在开始标签中进行关闭（**以开始标签的结束而结束**）
- 大多数 HTML 元素可拥有属性

## 嵌套的 HTML 元素

大多数 HTML 元素可以嵌套（可以包含其他 HTML 元素）。
HTML 文档由嵌套的 HTML 元素构成。

HTML 文档实例
```html
<html>

<body>
<p>This is my first paragraph.</p>
</body>

</html>

<!-- 上面的例子包含三个 HTML 元素 -->
```

## HTML 实例解释

### `<p>` 元素

```html
<p>This is my first paragraph.</p>
```
这个 `<p>` 元素定义了 HTML 文档中的一个段落。
这个元素拥有一个开始标签 `<p>`，以及一个结束标签 `</p>`。
元素内容是：This is my first paragraph。

### `<body>` 元素

```html
<body>
<p>This is my first paragraph.</p>
</body>
```
`<body>` 元素定义了 HTML 文档的主体。
这个元素拥有一个开始标签 `<body>`，以及一个结束标签 `</body>`。
元素内容是另一个 HTML 元素（p 元素）。

### `<html>` 元素

```html
<html>

<body>
<p>This is my first paragraph.</p>
</body>

</html>
```
`<html>` 元素定义了整个 HTML 文档。
这个元素拥有一个开始标签 `<html>`，以及一个结束标签 `</html>`。
元素内容是另一个 HTML 元素（body 元素）。

### 不要忘记结束标签

即使您忘记了使用结束标签，大多数浏览器也会正确地显示 HTML：
```htnl
<p>This is a paragraph
<p>This is a paragraph
```
上面的例子在大多数浏览器中都没问题，但不要依赖这种做法。忘记使用结束标签会产生不可预料的结果或错误。
> 注释：未来的 HTML 版本不允许省略结束标签。

### 空的 HTML 元素
没有内容的 HTML 元素被称为空元素。空元素是在开始标签中关闭的。
`<br>` 就是没有关闭标签的空元素（`<br>` 标签定义换行）。
在 XHTML、XML 以及未来版本的 HTML 中，所有元素都必须被关闭。
在开始标签中添加斜杠，比如 `<br />`，是<font color=blue>关闭空元素的正确方法</font>，HTML、XHTML 和 XML 都接受这种方式。
即使 `<br>` 在所有浏览器中都是有效的，但使用 `<br />` 其实是更长远的保障。

### HTML 提示：使用小写标签

HTML 标签对大小写不敏感：`<P>` 等同于 `<p>`。许多网站都使用大写的 HTML 标签。
W3School 使用的是小写标签，因为万维网联盟（W3C）在 HTML 4 中推荐使用小写，而<font color=red>在未来 (X)HTML 版本中强制使用小写</font>。

# HTML 属性

<font color=red size=5>属性为 HTML 元素提供附加信息</font>。
- HTML 标签可以拥有属性。属性提供了有关 HTML 元素的更多的信息。
- 属性总是以名称/值对的形式出现，比如：name="value"。
- 属性总是在 HTML 元素的开始标签中规定。

## 属性实例

HTML 链接由 `<a>` 标签定义。链接的地址在 href 属性中指定：
`<a href="http://www.w3school.com.cn">This is a link</a>`

### 属性例子 1

`<h1>` 定义标题的开始。
`<h1 align="center">` 拥有关于对齐方式的附加信息。
```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">

<html>

<body>

<h1 align="center">This is heading 1</h1>

<p>上面的标题在页面中进行了居中排列。上面的标题在页面中进行了居中排列。上面的标题在页面中进行了居中排列。</p>

</body>
</html>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/属性例子1-标题对其方式.png" alt="属性例子1-标题对其方式"  title="属性例子1-标题对其方式" width="600" height="" /></center>

### 属性例子 2

`<body>` 定义 HTML 文档的主体。
`<body bgcolor="yellow">` 拥有关于背景颜色的附加信息。
```html
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<meta http-equiv="Content-Language" content="zh-cn" />
</head>

<body bgcolor="yellow">
<h2>请看: 改变了颜色的背景。</h2>
</body>

</html>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTML背景颜色属性.png" alt="HTML背景颜色属性"  title="HTML背景颜色属性" width="600" height="" /></center>

属性例子 3
`<table>` 定义 HTML 表格。（您将在稍后的章节学习到更多有关 HTML 表格的内容）

`<table border="1">` 拥有关于表格边框的附加信息。

### 属性例子 3

`<table>` 定义 HTML 表格。（您将在稍后的章节学习到更多有关 HTML 表格的内容）
`<table border="1">` 拥有关于表格边框的附加信息。

## HTML 提示：使用小写属性

属性和属性值对大小写不敏感。
不过，万维网联盟在其 HTML 4 推荐标准中推荐小写的属性/属性值。
而新版本的 (X)HTML 要求使用小写属性。

## 始终为属性值加引号
属性值应该始终被包括在引号内。双引号是最常用的，不过使用单引号也没有问题。

在某些个别的情况下，比如属性值本身就含有双引号，那么您必须使用单引号，例如：
`name='Bill "HelloWorld" Gates'`

## HTML 属性参考手册
我们的完整的 HTML 参考手册提供了每个 HTML 元素可使用的合法属性的完整列表：
[HTML 参考手册](https://www.w3school.com.cn/tags/index.asp)
[HTML 全局属性](https://www.w3school.com.cn/tags/html_ref_standardattributes.asp)

下面列出了适用于大多数 HTML 元素的属性：

| 属性  | 值               | 描述                                     |
| ----- | ---------------- | ---------------------------------------- |
| class | classname        | 规定元素的类名（classname）              |
| id    | id               | 规定元素的唯一 id                        |
| style | style_definition | 规定元素的行内样式（inline style）       |
| title | text             | 规定元素的额外信息（可在工具提示中显示） |

# HTML 标题

标题（Heading）是通过 `<h1>` - `<h6>` 等标签进行定义的。
`<h1>` 定义最大的标题。`<h6>` 定义最小的标题。
实例
```html
<h1>This is a heading</h1>
<h2>This is a heading</h2>
<h3>This is a heading</h3>
```
> 注释：浏览器会自动地在标题的前后添加空**行**。
> 注释：默认情况下，HTML 会自动地在块级元素前后添加一个额外的空**行**，比如段落、标题元素前后。

标题很重要
- 请确保将 HTML heading 标签只用于标题。不要仅仅是为了产生粗体或大号的文本而使用标题。
- 搜索引擎使用标题为您的网页的结构和内容编制索引。
- 因为用户可以通过标题来快速浏览您的网页，所以用标题来呈现文档结构是很重要的。
- 应该将 h1 用作主标题（最重要的），其后是 h2（次重要的），再其次是 h3，以此类推。

## HTML 水平线

`<hr />` 标签在 HTML 页面中创建水平线。
hr 元素可用于分隔内容。
实例
```html
<p>This is a paragraph</p>
<hr />
<p>This is a paragraph</p>
<hr />
<p>This is a paragraph</p>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTML水平线hr标签.png" alt="HTML水平线hr标签"  title="HTML水平线hr标签" width="600" height="" /></center>

> 提示：使用水平线 (`<hr>` 标签) 来分隔文章中的小节是一个办法（但并不是唯一的办法）。

## HTML 注释
可以将注释插入 HTML 代码中，这样可以提高其可读性，使代码更易被人理解。浏览器会忽略注释，也不会显示它们。
注释是这样写的：
实例
`<!-- This is a comment -->`
> 注释：开始括号之后（左边的括号）需要紧跟一个叹号，结束括号之前（右边的括号）不需要。
> 提示：合理地使用注释可以对未来的代码编辑工作产生帮助。

## HTML 提示 - 如何查看源代码

您一定曾经在看到某个网页时惊叹道 “WOW! 这是如何实现的？”
如果您想找到其中的奥秘，只需要单击右键，然后选择“查看源文件”（IE）或“<font color=red>查看页面源代码</font>”（Firefox），其他浏览器的做法也是类似的。这么做会打开一个包含页面 HTML 代码的窗口。

## HTML 标签参考手册

[Back to HTMLNotebook](#HTMLNotebook)

W3School 的标签参考手册提供了有关这些标题及其属性的更多信息。
您将在本教程下面的章节中学到更多有关 HTML 标签和属性的知识。

| 标签             | 描述             |
| ---------------- | ---------------- |
| `<html>`         | 定义 HTML 文档。 |
| `<body>`         | 定义文档的主体。 |
| `<h1>` to `<h6>` | 定义 HTML 标题   |
| `<hr>`           | 定义水平线。     |
| `<!-->`          | 定义注释。       |

# HTML 段落

可以把 HTML 文档分割为若干段落。
段落是通过 <p> 标签定义的。
实例
```html
<p>This is a paragraph</p>
<p>This is another paragraph</p>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTML段落标签p.png" alt="HTML段落标签p"  title="HTML段落标签p" width="600" height="" /></center>

> 注释：浏览器会自动地在段落的前后添加空行。（`<pre>` 是块级元素）
> 提示：使用空的段落标记 `<p></p>` 去插入一个空行是个坏习惯。用 `<br />` 标签代替它！（但是不要用 `<br />` 标签去创建列表。不要着急，您将在稍后的篇幅学习到 HTML 列表。）

## HTML 折行

如果您希望在不产生一个新段落的情况下进行换行（新行），请使用 `<br />` 标签：
`<p>This is<br />a para<br />graph with line breaks</p>`

> <br /> 元素是一个空的 HTML 元素。由于关闭标签没有任何意义，因此它没有结束标签。

## HTML 输出 - 有用的提示

我们无法确定 HTML 被显示的确切效果。屏幕的大小，以及对窗口的调整都可能导致不同的结果。
对于 HTML，您无法通过在 HTML 代码中添加额外的空格或换行来改变输出的效果。
当显示页面时，浏览器会移除源代码中多余的空格和空行。所有连续的空格或空行都会被算作一个空格。需要注意的是，HTML 代码中的所有连续的空行（换行）也被显示为一个空格。

# HTML 样式

style 属性用于改变 HTML 元素的样式。
style 属性的作用：
**提供了一种改变所有 HTML 元素的样式的通用方法**。
样式是 HTML 4 引入的，它是一种新的首选的改变 HTML 元素样式的方式。通过 HTML 样式，能够通过使用 style 属性直接将样式添加到 HTML 元素，或者间接地在独立的样式表中（CSS 文件）进行定义。
您可以在我们的 [CSS 教程](https://www.w3school.com.cn/css/index.asp)中学习关于样式和 CSS 的所有知识。
在我们的 HTML 教程中，我们将使用 style 属性向您讲解 HTML 样式。

## 不赞成使用的标签和属性

在 HTML 4 中，有若干的标签和属性是被废弃的。被废弃（Deprecated）的意思是在未来版本的 HTML 和 XHTML 中将不支持这些标签和属性。
这里传达的信息很明确：请避免使用这些被废弃的标签和属性！

**应该避免使用下面这些标签和属性 , 请使用样式代替！：**

| 标签                     | 描述             |
| ------------------------ | ---------------- |
| `<center>`               | 定义居中的内容。 |
| `<font>` 和 `<basefont>` | 定义 HTML 字体。 |
| `<s>` 和 `<strike>`      | 定义删除线文本   |
| `<u>`                    | 定义下划线文本   |

| 属性    | 描述               |
| ------- | ------------------ |
| align   | 定义文本的对齐方式 |
| bgcolor | 定义背景颜色       |
| color   | 定义文本颜色       |

## HTML 样式实例 - 背景颜色

background-color 属性为元素定义了背景颜色：
```html
<html>

<body style="background-color:yellow">
<h2 style="background-color:red">This is a heading</h2>
<p style="background-color:green">This is a paragraph.</p>
</body>

</html>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/HTML样式style背景色background-color.png" alt="HTML样式style背景色background-color"  title="HTML样式style背景色background-color" width="600" height="" /></center>

> style 属性淘汰了“旧的” bgcolor 属性。

## HTML 样式实例 - 字体、颜色和尺寸

font-family、color 以及 font-size 属性分别定义元素中文本的字体系列、颜色和字体尺寸：
```html
<html>

<body>
<h1 style="font-family:verdana">A heading</h1>
<p style="font-family:arial;color:red;font-size:20px;">A paragraph.</p>
</body>

</html>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/HTML样式style字体颜色尺寸.png" alt="HTML样式style字体颜色尺寸"  title="HTML样式style字体颜色尺寸" width="600" height="" /></center>

> style 属性淘汰了旧的 <font> 标签

## HTML 样式实例 - 文本对齐

text-align 属性规定了元素中文本的水平对齐方式：
```html
<html>

<body>
<h1 style="text-align:center">This is a heading</h1>
<p>The heading above is aligned to the center of this page.</p>
</body>

</html>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115220504.png" alt="20200115220504"  title="HTML样式style文本对齐方式" width="600" height="" /></center>

> style 属性淘汰了旧的 "align" 属性。

# HTML 文本格式化

HTML 可定义很多供格式化输出的元素，比如粗体和斜体字。
[HTML 教程延伸阅读：改变文本的外观和含义](https://www.w3school.com.cn/html/html_style.asp)

## HTML 文本格式化实例

如何在一个 HTML 文件中对文本进行格式化
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115220856.png" alt="20200115220856"  title="HTML文本格式化" width="600" height="" /></center>

如何使用 pre 标签对空行和空格进行控制。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115222847.png" alt="20200115222847"  title="预格式文本" width="600" height="" /></center>

不同的“计算机输出”标签的显示效果
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115222338.png" alt="20200115222338"  title="HTML计算机输出标签的显示效果" width="600" height="" /></center>

如何在 HTML 文件中写地址。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115223105.png" alt="20200115223105"  title="HTML中写链接地址" width="600" height="" /></center>

如何实现缩写或首字母缩写。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115223551.png" alt="20200115223551"  title="缩写或首字母缩写" width="600" height="" /></center>

如何改变文字的方向。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115223755.png" alt="20200115223755"  title="变文字的方向逆序" width="600" height="" /></center>

如何实现长短不一的引用语。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115224009.png" alt="20200115224009"  title="长短不一的引用语" width="600" height="" /></center>



如何标记删除文本和插入文本。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115224152.png" alt="20200115224152"  title="标记删除文本和插入文本" width="600" height="" /></center>

## 如何查看 HTML 源码

您是否有过这样的经历，当你看到一个很棒的站点，你会很想知道开发人员是如何将它实现的？

你有没有看过一些网页，并且想知道它是如何做出来的呢？

要揭示一个网站的技术秘密，其实很简单。单击浏览器的“查看”菜单，选择“查看源文件”即可。随后你会看到一个弹出的窗口，窗口内就是实际的 HTML 代码。

## 文本格式化标签

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115224300.png" alt="20200115224300"  title="文本格式化标签" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115224449.png" alt="20200115224449"  title="引用和术语定义" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115224401.png" alt="20200115224401"  title="计算机输出标签" width="600" height="" /></center>

# HTML 引用Quotation

HTML `<q>` 用于短的引用
HTML `<q>` 元素定义短的引用。

浏览器通常会为 `<q>` 元素包围引号。

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116085827.png" alt="20200116085827"  title="HTML短引用" width="600" height="" /></center>

## 用于长引用的 HTML <blockquote>

HTML `<blockquote>` 元素定义被引用的节。
浏览器通常会对 `<blockquote>` 元素进行缩进处理。
```html
<p>以下内容引用自 WWF 的网站：</p>
<blockquote cite="http://www.worldwildlife.org/who/index.html">

五十年来，WWF 一直致力于保护自然界的未来。
世界领先的环保组织，WWF 工作于 100 个国家，
并得到美国一百二十万会员及全球近五百万会员的支持。
</blockquote>
```

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116090319.png" alt="20200116090319"  title="HTML长引用" width="600" height="" /></center>

## 用于缩略词的 HTML `<abbr>`

HTML `<abbr>` 元素定义缩写或首字母缩略语。
对缩写进行标记能够为浏览器、翻译系统以及搜索引擎提供有用的信息。
<p><abbr title="World Health Organization">WHO</abbr> 成立于 1948 年。</p>
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116090814.png" alt="20200116090814"  title="HTML缩略词abbr" width="600" height="" /></center>

## 用于定义的 HTML <dfn>

HTML `<dfn>` 元素定义项目或缩写的定义。
`<dfn>` 的用法，按照 HTML5 标准中的描述，有点复杂：

1. 如果设置了 `<dfn>` 元素的 title 属性，则定义项目：
```html
<p><dfn title="World Health Organization">WHO</dfn> 成立于 1948 年。</p>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116112516.png" alt="20200116112516"  title="HTML定义元素dfn" width="600" height="" /></center>

2. 如果 <dfn> 元素包含具有标题的 <abbr> 元素，则 title 定义项目：
```html
<p><dfn><abbr title="World Health Organization">WHO</abbr></dfn> 成立于 1948 年。</p>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116112955.png" alt="20200116112955"  title="HTML定义dfn元素包含标题的abbr元素" width="600" height="" /></center>

3. 否则，<dfn> 文本内容即是项目，并且父元素包含定义。
```html
<p><dfn>WHO</dfn> World Health Organization 成立于 1948 年。</p>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116113249.png" alt="20200116113249"  title="HTML定义dfn元素文本内容即项目" width="600" height="" /></center>

> 注释：如果您希望简而化之，请使用第一条，或使用 <abbr> 代替。

## 用于联系信息的 HTML <address>

HTML `<address>` 元素定义文档或文章的联系信息（作者/拥有者）。
此元素通常以斜体显示。大多数浏览器会在此元素前后添加折行。
```html
<address>
Written by Donald Duck.<br> 
Visit us at:<br>
Example.com<br>
Box 564, Disneyland<br>
USA
</address>
```

## 用于著作标题的 HTML `<cite>`

HTML `<cite>` 元素定义著作的标题。
浏览器通常会以斜体显示 `<cite>` 元素。

<p><cite>The Scream</cite> by Edward Munch. Painted in 1893.</p>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116113838.png" alt="20200116113838"  title="HTML著作标题引用cite" width="600" height="" /></center>

## 用于双向重写的 HTML `<bdo>`
HTML `<bdo>` 元素定义双流向覆盖（bi-directional override）。
`<bdo>` 元素用于覆盖当前文本方向：
```html
<bdo dir="rtl">This text will be written from right to left</bdo>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116114242.png" alt="20200116114242"  title="HTML双向重写" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116114349.png" alt="20200116114349"  title="HTML 引文引用和定义元素" width="600" height="" /></center>

# HTML 计算机代码元素

```js
var person = {
    firstName:"Bill",
    lastName:"Gates",
    age:50,
    eyeColor:"blue"
}
```

## HTML 计算机代码格式

通常，HTML 使用可变的字母尺寸，以及可变的字母间距。
在显示计算机代码示例时，并不需要如此。
`<kbd>`, `<samp>`, 以及 `<code>` 元素全都支持固定的字母尺寸和间距。

## HTML 键盘格式

HTML `<kbd>` 元素定义键盘输入：
```html
<p>To open a file, select:</p>
<p><kbd>File | Open...</kbd></p>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116114959.png" alt="20200116114959"  title="HTML键盘格式元素kbd" width="600" height="" /></center>

## HTML 样本格式

HTML `<samp>` 元素定义计算机输出示例：

```html
<samp>
demo.example.com login: Apr 12 09:10:17

Linux 2.6.10-grsec+gg3+e+fhs6b+nfs+gr0501+++p3+c4a+gr2b-reslog-v6.189
</samp>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116115435.png" alt="20200116115435"  title="样本格式元素samp定义计算机输出示例" width="600" height="" /></center>

## HTML 代码格式
HTML `<code>` 元素定义编程代码示例：
```html
<code>
var person = { firstName:"Bill", lastName:"Gates", age:50, eyeColor:"blue" }
</code>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116115640.png" alt="20200116115640"  title="代码格式code" width="600" height="" /></center>

> `<code>` 元素不保留多余的空格和折行：

```html
<p>Coding Example:</p>

<code>
var person = {
    firstName:"Bill",
    lastName:"Gates",
    age:50,
    eyeColor:"blue"
}
</code>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116115846.png" alt="20200116115846"  title="代码格式code不保留多余的空格和折行" width="600" height="" /></center>

> 如需保留多余的空格和折行，您必须在 <pre> 元素中包围代码：

```html
<p>Coding Example:</p>

<code>
<pre>
var person = {
    firstName:"Bill",
    lastName:"Gates",
    age:50,
    eyeColor:"blue"
}
</pre>
</code>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116120049.png" alt="20200116120049"  title="代码格式code加pre保留多余的空格和折行" width="600" height="" /></center>

## HTML 变量格式化
HTML <var> 元素定义数学变量：
```html
<p>Einstein wrote:</p>

<p><var>E = m c<sup>2</sup></var></p>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116120321.png" alt="20200116120321"  title="HTML 计算机代码元素标签" width="600" height="" /></center>

# HTML 注释

注释标签 `<!-- 与 -->` 用于在 HTML 插入注释。
> 注释：在开始标签中有一个惊叹号，但是结束标签中没有。
浏览器不会显示注释，但是能够帮助记录您的 HTML 文档。
您可以利用注释在 HTML 中放置通知和提醒信息：
```html
<!-- 这是一段注释 -->

<p>这是一个段落。</p>

<!-- 记得在此处添加信息 -->
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116120646.png" alt="20200116120646"  title="HTML 注释" width="600" height="" /></center>

## 条件注释

您也许会在 HTML 中偶尔发现条件注释：
```html
<!--[if IE 8]>
    .... some HTML here ....
<![endif]-->
```
> 条件注释定义只有 Internet Explorer 执行的 HTML 标签。

## 软件程序标签

各种 HTML 软件程序也能够生成 HTML 注释。
例如 `<!--webbot bot-->` 标签会被包围在由 FrontPage 和 Expression Web 创建的 HTML 注释中。
作为一项规则，这些标签的存在，有助于对创建这些标签的软件的支持。

# HTML CSS

通过使用 HTML4.0，所有的格式化代码均可移出 HTML 文档，然后移入一个独立的样式表。

如何使用添加到 `<head>` 部分的样式信息对 HTML 进行格式化。
```html
<html>

<head>
<style type="text/css">
h1 {color: red}
p {color: blue}
</style>
</head>

<body>
<h1>header 1</h1>
<p>A paragraph.</p>
</body>

</html>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116141908.png" alt="20200116141908"  title="添加到 head部分的样式信息对 HTML 进行格式化" width="600" height="" /></center>

如何使用样式属性做一个没有下划线的链接。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116142706.png" alt="20200116142706"  title="使用样式style属性做一个没有下划线的链接" width="600" height="" /></center>

如何 `<link>` 标签链接到一个外部样式表。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116144050.png" alt="20200116144050"  title="link标签链接到一个外部样式表" width="600" height="" /></center>

## 如何使用样式

当浏览器读到一个样式表，它就会按照这个样式表来对文档进行格式化。有以下三种方式来插入样式表：
1. 外部样式表
当样式需要被应用到很多页面的时候，外部样式表将是理想的选择。使用外部样式表，你就可以通过更改一个文件来改变整个站点的外观。
```html
<head>
<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>
```

2. 内部样式表
当单个文件需要特别样式时，就可以使用内部样式表。你可以在 head 部分通过 `<style>` 标签定义内部样式表。
```html
<html>
<head>

<style type="text/css">
body {background-color: red}
p {margin-left: 200px}
</style>
</head>

<body><p>我引用了内部样式表</p></body>
</html>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116144908.png" alt="20200116144908"  title="在 head 部分通过style标签定义内部样式表" width="600" height="" /></center>

3. 内联样式
当特殊的样式需要应用到个别元素时，就可以使用内联样式。 使用内联样式的方法是在相关的标签中使用样式属性。样式属性可以包含任何 CSS 属性。以下实例显示出如何改变段落的颜色和左外边距。
```html
<p style="color: red; margin-left: 200px">
This is a paragraph
</p>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116145229.png" alt="20200116145229"  title="20200116145229" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116145426.png" alt="20200116145426"  title="常见样式标签" width="600" height="" /></center>

# HTML 链接

[什么是超文本？](https://www.w3school.com.cn/tags/tag_term_hypertext.asp)

HTML 使用超级链接与网络上的另一个文档相连。
几乎可以在所有的网页中找到链接。点击链接可以从一张页面跳转到另一张页面。

如何在 HTML 文档中创建链接。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116145953.png" alt="20200116145953"  title="HTML 文档中创建链接" width="600" height="" /></center>

如何使用图像作为链接。
```html
<html>

<body>
<p>
您也可以使用图像来作链接：
<a href="/example/html/lastpage.html">
<img border="0" src="/i/eg_buttonnext.gif" />
</a>
</p>

</body>
</html>
```
<a href="https://www.w3school.com.cn/tiy/t.asp?f=html_imglink">
<center><img border="0" src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/buttonnext.png" alt="buttonnext"  title="buttonnext图像作为链接" width="600" height="" /></center>
</a>

如何在新窗口打开一个页面，这样的话访问者就无需离开你的站点了。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116151647.png" alt="20200116151647"  title=" target 属性设置为 '_blank'该链接会在新窗口中打开" width="600" height="" /></center>

如何使用链接跳转至文档的另一个部分
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116155017.png" alt="20200116155017"  title="使用链接跳转至文档的另一个部分" width="600" height="" /></center>

如何跳出框架，假如你的页面被固定在框架之内。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116155450.png" alt="20200116155450"  title="跳出框架" width="600" height="" /></center>

如何链接到一个邮件。（本例在安装邮件客户端程序后才能工作。）
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116194635.png" alt="20200116194635"  title="链接到一个邮件" width="600" height="" /></center>

更加复杂的邮件链接
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116194820.png" alt="20200116194820"  title="更加复杂的邮件链接" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116194858.png" alt="20200116194858"  title="HTML 链接标签" width="600" height="" /></center>

# HTML 图像

> 参考
[HTML Image Tag Generator - 𝗧𝗛𝗘 𝗕𝗘𝗦𝗧 𝗛𝗧𝗠𝗟 𝗖𝗢𝗗𝗘 𝗪𝗜𝗭𝗔𝗥𝗗](https://html-css-js.com/html/generator/image/)

<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119211244.png" alt="20200119211244"  title="HTML Image Tag Generator" width="600" height="" /><figcaption><font color=green>HTML Image Tag Generator</font></figcaption></center></figure>

通过使用 HTML，可以在文档中显示图像。
如何在网页中显示图像。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116195534.png" alt="20200116195534"  title="网页中显示图像" width="600" height="" /></center>

如何将其他文件夹或服务器的图片显示到网页中。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116195729.png" alt="20200116195729"  title="将其他文件夹或服务器的图片显示到网页中" width="600" height="" /></center>

如何向 HTML 页面添加背景图片。
```html
<html>

<body background="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/eg_cute.gif">

<h3>图像背景</h3>

<p>gif 和 jpg 文件均可用作 HTML 背景。</p>

<p>如果图像小于页面，图像会进行重复。</p>

</body>
</html>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/d9492d2e-0e88-46e9-9bc4-2c273e6cab25.gif" alt="d9492d2e-0e88-46e9-9bc4-2c273e6cab25"  title="HTML 页面添加背景图片" width="600" height="" /></center>

如何在文字中排列图像
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116201255.png" alt="20200116201255"  title="文字中排列图像" width="600" height="" /></center>

如何使图片浮动至段落的左边或右边。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116201438.png" alt="20200116201438"  title="图片浮动至段落的左边或右边" width="600" height="" /></center>

如何将图片调整到不同的尺寸。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116201618.png" alt="20200116201618"  title="图片调整到不同的尺寸" width="600" height="" /></center>

如何为图片显示替换文本。在浏览器无法载入图像时，替换文本属性告诉读者们失去的信息。为页面上的图像都加上替换文本属性是个好习惯。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116201832.png" alt="20200116201832"  title="alt属性为图片显示替换文本" width="600" height="" /></center>

如何将图像作为一个链接使用。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116202000.png" alt="20200116202000"  title="将图像作为一个链接使用" width="600" height="" /></center>

如何创建带有可供点击区域的图像地图。其中的每个区域都是一个超级链接。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116202521.png" alt="20200116202521"  title="区域的图像地图" width="600" height="" /></center>

如何把一幅普通的图像设置为图像映射。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116202846.png" alt="20200116202846"  title="普通的图像设置为图像映射" width="600" height="" /></center>

## 图像标签（`<img>`）和源属性（Src）

在 HTML 中，图像由 `<img>` 标签定义。
`<img>` 是空标签，意思是说，它只包含属性，并且没有闭合标签。
要在页面上显示图像，你需要使用源属性（src）。src 指 "source"。源属性的值是图像的 URL 地址。
`<img src="url" />`

## 替换文本属性（Alt）

alt 属性用来为图像定义一串预备的可替换的文本。替换文本属性的值是用户定义的。
`<img src="boat.gif" alt="Big Boat">`
在浏览器无法载入图像时，替换文本属性告诉读者她们失去的信息。此时，浏览器将显示这个替代性的文本而不是图像。为页面上的图像都加上替换文本属性是个好习惯，这样有助于更好的显示信息，并且对于那些使用纯文本浏览器的人来说是非常有用的。

## HTML5 `<figure>` 和 `<figcaption>` 元素

<img> 元素定义图像，<figcaption> 元素定义标题。

在书籍和报纸中，与图片搭配的标题很常见。
标题（caption）的作用是为图片添加可见的解释。
通过 HTML5，图片和标题能够被组合在 `<figure>` 元素中：
```html
<figure>
   <center>
   <img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117171735.png" alt="20200117171735"  title="带有 HTML5 DOCTYPE 的 HTML 文档" width="600" height="" />
   <figcaption>Fig1. - The Pulpit Pock, Norway.</figcaption>
   </center>
</figure>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200118144931.png" alt="20200118144931"  title="20200118144931" width="600" height="" /></center>

## 基本的注意事项 - 有用的提示：

假如某个 <font color=red>HTML 文件</font>包含十个图像，那么为了正确显示这个页面，需要加载 11 个文件。加载图片是需要时间的，所以我们的建议是：<font color=red>慎用图片</font>。

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116202943.png" alt="20200116202943"  title="图像标签" width="600" height="" /></center>

# HTML 表格

> 参考
[HTML Table Styler ▦ CSS Generator | 𝗗𝗜𝗩𝗧𝗔𝗕𝗟𝗘.𝗖𝗢𝗠](https://divtable.com/table-styler/)

<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119210703.png" alt="20200119210703"  title="HTML Table Styler ▦ CSS Generator" width="600" height="" /><figcaption><font color=green>HTML Table Styler ▦ CSS Generator</font></figcaption></center></figure>

1. 表格由 `<table>` 标签来定义。
2. 每个表格均有若干行（由 `<tr>` 标签定义），字母 tr 指表格行（table row）。
3. 每行被分割为若干单元格（由 `<td>` 标签定义）, 字母 td 指表格数据（table data），即数据单元格的内容。

数据单元格可以包含文本、图片、列表、段落、表单、水平线、表格等等。



如何在 HTML 文档中创建表格
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116204333.png" alt="20200116204333"  title="创建表格" width="600" height="" /></center>

各种类型的表格边框
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116204538.png" alt="20200116204538"  title="表格边框" width="600" height="" /></center>

## 表格和边框属性

如果不定义边框属性，表格将不显示边框。有时这很有用，但是大多数时候，我们希望显示边框。

使用边框属性来显示一个带有边框的表格：
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116205207.png" alt="20200116205207"  title="边框属性border" width="600" height="" /></center>

## 表格的表头

表格的表头使用 `<th>` 标签进行定义。
大多数浏览器会把表头显示为粗体居中的文本：
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116205405.png" alt="20200116205405"  title="表格的表头标签th" width="600" height="" /></center>

如何水平或竖直地显示表格表头
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116210510.png" alt="20200116210510"  title="水平或竖直地显示表格表头" width="600" height="" /></center>

## 表格中的空单元格

在一些浏览器中，没有内容的表格单元显示得不太好。如果某个单元格是空的（没有内容），浏览器可能无法显示出这个单元格的边框。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116210133.png" alt="20200116210133"  title="表格中的空单元格" width="600" height="" /></center>

正如您看到的，其中一个单元没有边框。这是因为它是空的。在该单元中插入一个空格后，仍然没有边框。
我们的技巧是在单元中插入一个 no-breaking 空格。
no-breaking 空格是一个字符实体。如果您不清楚什么是字符实体，请阅读关于字符实体的章节。
no-breaking 空格由和号开始 ("&")，然后是字符"nbsp"，并以分号结尾(";")。

## 带有标题的表格caption

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116210958.png" alt="20200116210958"  title="带有标题的表格" width="600" height="" /></center>

## 定义跨行或跨列的表格单元格
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116211411.png" alt="20200116211411"  title="跨行或跨列的表格单元格" width="600" height="" /></center>

## 在不同的元素内显示元素

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116213200.png" alt="20200116213200"  title="不同的元素内显示元素" width="600" height="" /></center>

> Markdown 不支持border属性，表格异常

## Cell padding 来创建单元格内容与其边框之间的空白

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116215318.png" alt="20200116215318"  title="20200116215318" width="600" height="" /></center>

## Cell spacing 增加单元格之间的距离

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116215526.png" alt="20200116215526"  title="20200116215526" width="600" height="" /></center>

## 向表格添加背景

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116215746.png" alt="20200116215746"  title="表格添加背景" width="600" height="" /></center>

## 向一个或者更多表格单元添加背景

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116220020.png" alt="20200116220020"  title="一个或者更多表格单元添加背景" width="600" height="" /></center>

## align 属性排列单元格内容

排列单元格内容,以便创建一个美观的表格
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116220232.png" alt="20200116220232"  title="align 属性排列单元格内容" width="600" height="" /></center>

## frame 属性来控制围绕表格的边框

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116220857.png" alt="20200116220857"  title=" frame属性来控制围绕表格的边框" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116221032.png" alt="20200116221032"  title="表格标签" width="600" height="" /></center>

# HTML 列表

> 参考
[HTML List Tag Generator - 𝗧𝗛𝗘 𝗕𝗘𝗦𝗧 𝗛𝗧𝗠𝗟 𝗖𝗢𝗗𝗘 𝗪𝗜𝗭𝗔𝗥𝗗](https://html-css-js.com/html/generator/list/)

<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119213732.png" alt="20200119213732"  title="HTML List Tag Generator" width="600" height="" /><figcaption><font color=green>HTML List Tag Generator</font></figcaption></center></figure>




HTML 支持有序、无序和定义列表

## 无序列表

无序列表是一个项目的列表，此列项目使用粗体圆点（典型的小黑圆圈）进行标记。

无序列表始于 `<ul>` 标签。每个列表项始于 `<li>`。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116221452.png" alt="20200116221452"  title="无序列表" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116222129.png" alt="20200116222129"  title="不同类型的无序列表" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116222506.png" alt="20200116222506"  title="嵌套列表" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116222728.png" alt="20200116222728"  title="嵌套列表" width="600" height="" /></center>

## 有序列表

同样，有序列表也是一列项目，列表项目使用数字进行标记。

有序列表始于 `<ol>` 标签。每个列表项始于 `<li>` 标签。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116221621.png" alt="20200116221621"  title="有序列表" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116222326.png" alt="20200116222326"  title="不同类型的有序列表" width="600" height="" /></center>

## 定义列表

自定义列表不仅仅是一列项目，而是项目及其注释的组合。

自定义<font color=red></font>列表以 `<dl>` 标签开始</font>。每个自定义<font color=orange></font>列表项以 `<dt>` 开始</font>。每个自定义<font color=blue></font>列表项的定义以 `<dd>` 开始</font>。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116221807.png" alt="20200116221807"  title="自定义列表" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116222824.png" alt="20200116222824"  title="20200116222824" width="600" height="" /></center>

# HTML 块元素

可以通过 `<div>` 和 `<span>` 将 HTML 元素组合起来。

## HTML 块

大多数 HTML 元素被定义为块级元素或内联元素。

编者注：“块级元素”译为 block level element，“内联元素”译为 inline element。

块级元素在浏览器显示时，通常会以新行来开始（和结束）。

例子：`<h1>, <p>, <ul>, <table>`

## HTML 内联元素

内联元素在显示时通常不会以新行开始。

例子：`<b>, <td>, <a>, <img>`

## HTML `<div>`<font color=red>块级</font>元素

HTML `<div>` 元素是块级元素，它是可用于组合其他 HTML 元素的容器。

`<div>` <font color=red>元素没有特定的含义</font>。除此之外，由于它属于块级元素，浏览器会在其前后显示折行。

如果与 CSS 一同使用，`<div>` 元素<font color=red>可用于对大的内容块设置样式属性</font>。

`<div>` 元素的另一个常见的用途是文档布局。它取代了使用表格定义布局的老式方法。使用 `<table>` 元素进行文档布局不是表格的正确用法。`<table>` 元素的作用是显示表格化的数据。

## HTML `<span>` <font color=blue>内联</font>元素

HTML `<span>` 元素是 <font color=blue>内联元素，可用作文本的容器</font>。

`<span>` 元素<font color=blue>也没有特定的含义</font>。

当与 CSS 一同使用时，`<span>` 元素可用于<font color=blue>为部分文本设置样式属性</font>。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116223723.png" alt="20200116223723"  title="HTML 分组标签" width="600" height="" /></center>

# HTML 类

对 HTML 进行分类（设置类），使我们能够为元素的类定义 CSS 样式。

为相同的类设置相同的样式，或者为不同的类设置不同的样式。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116224248.png" alt="20200116224248"  title="元素的类定义 CSS 样式" width="600" height="" /></center>

## 分类块级元素

HTML `<div>` 元素是块级元素。它能够用作其他 HTML 元素的容器。

设置 `<div>` 元素的类，使我们能够为相同的 `<div>` 元素设置相同的类：
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116224541.png" alt="20200116224541"  title="相同的div块级元素设置相同的类" width="600" height="" /></center>

## 分类行内元素

HTML `<span>` 元素是行内元素，能够用作文本的容器。

设置 `<span>` 元素的类，能够为相同的 `<span>` 元素设置相同的样式。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116225044.png" alt="20200116225044"  title="相同的span行内元素设置相同的样式" width="600" height="" /></center>

# HTML 布局

网站常常以多列显示内容（就像杂志和报纸）。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117092251.png" alt="20200117092251"  title="HTML 布局" width="600" height="" /></center>

## 使用 `<div>` 元素的 HTML 布局

注释：`<div>` 元素常用作布局工具，因为能够轻松地通过 CSS 对其进行定位。

这个例子使用了四个 `<div>` 元素来创建多列布局：

### div块级元素标签
```html
<body>

<div id="header">
<h1>City Gallery</h1>
</div>

<div id="nav">
London<br>
Paris<br>
Tokyo<br>
</div>

<div id="section">
<h1>London</h1>
<p>
London is the capital city of England. It is the most populous city in the United Kingdom,
with a metropolitan area of over 13 million inhabitants.
</p>
<p>
Standing on the River Thames, London has been a major settlement for two millennia,
its history going back to its founding by the Romans, who named it Londinium.
</p>
</div>

<div id="footer">
Copyright W3School.com.cn
</div>

</body>

<style>
#header {
    background-color:black;
    color:white;
    text-align:center;
    padding:5px;
}
#nav {
    line-height:30px;
    background-color:#eeeeee;
    height:300px;
    width:100px;
    float:left;
    padding:5px; 
}
#section {
    width:350px;
    float:left;
    padding:10px; 
}
#footer {
    background-color:black;
    color:white;
    clear:both;
    text-align:center;
    padding:5px; 
}
</style>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117093005.png" alt="20200117093005"  title="div块级元素来创建多列布局" width="600" height="" /></center>

### Cascading Style Sheets - CSS-Style样式
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117093724.png" alt="20200117093724"  title="CSS-Style" width="600" height="" /></center>

## 使用 HTML5 的网站布局

HTML5 提供的新语义元素定义了网页的不同部分：

HTML5 语义元素

| header  | 定义文档或节的页眉             |
| ------- | ------------------------------ |
| nav     | 定义导航链接的容器             |
| section | 定义文档中的节                 |
| article | 定义独立的自包含文章           |
| aside   | 定义内容之外的内容（比如侧栏） |
| footer  | 定义文档或节的页脚             |
| details | 定义额外的细节                 |
| summary | 定义 details 元素的标题        |

这个例子使用 `<header>, <nav>, <section>`, 以及 `<footer>` 来创建多列布局：

```html
<body>

<header>
<h1>City Gallery</h1>
</header>

<nav>
London<br>
Paris<br>
Tokyo<br>
</nav>

<section>
<h1>London</h1>
<p>
London is the capital city of England. It is the most populous city in the United Kingdom,
with a metropolitan area of over 13 million inhabitants.
</p>
<p>
Standing on the River Thames, London has been a major settlement for two millennia,
its history going back to its founding by the Romans, who named it Londinium.
</p>
</section>

<footer>
Copyright W3School.com.cn
</footer>

</body>

<style>
header {
    background-color:black;
    color:white;
    text-align:center;
    padding:5px; 
}
nav {
    line-height:30px;
    background-color:#eeeeee;
    height:300px;
    width:100px;
    float:left;
    padding:5px; 
}
section {
    width:350px;
    float:left;
    padding:10px; 
}
footer {
    background-color:black;
    color:white;
    clear:both;
    text-align:center;
    padding:5px; 
}
```

### HTML5-body

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117094859.png" alt="20200117094859"  title="HTML5-body" width="600" height="" /></center>

### HTML5-Style

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117095215.png" alt="20200117095215"  title="HTML5-Style" width="600" height="" /></center>

## 使用表格的 HTML 布局

注释：`<table>` 元素不是作为布局工具而设计的。

`<table>` 元素的作用是显示表格化的数据。

使用 `<table>` 元素能够取得布局效果，因为能够通过 CSS 设置表格元素的样式：
```html
<body>

<table class="lamp">
<tr>
  <th>
    <img src="/images/lamp.jpg" alt="Note" style="height:32px;width:32px">
  </th>
  <td>
    The table element was not designed to be a layout tool.
  </td>
</tr>
<tr>
  <th>
    <img src="/images/lamp.jpg" alt="Note" style="height:32px;width:32px">
  </th>
  <td>
    The table element was not designed to be a layout tool.
  </td>
</tr>
</table>

</body>

<style>
table.lamp {
    width:100%;
    height:50%;
    border:5px solid orange;
}
table.lamp th, td {
	border:5px solid purple;
	background:yellow;
    padding:10px;
}
table.lamp td {
	background:blue;
	color:red;
    width:40px;
}
</style>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117101025.png" alt="20200117101025"  title="CSS 设置表格元素的样式" width="600" height="" /></center>

# HTML 响应式 Web 设计

什么是响应式 Web 设计？
- RWD 指的是响应式 Web 设计（Responsive Web Design）
- RWD 能够以可变尺寸传递网页
- RWD 对于平板和移动设备是必需的

## 创建您自己的响应式设计

创建响应式设计的一个方法，是自己来创建它：
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117105527.png" alt="创建您自己的响应式设计"  title="20200117105527" width="600" height="" /></center>

## 使用 Bootstrap

另一个创建响应式设计的方法，是<font color=red>使用现成的 CSS 框架</font>。

<font color=red>Bootstrap 是最流行的开发响应式 web 的 HTML, CSS, 和 JS 框架</font>。

如需学习更多有关 Bootstrap 的知识，请阅读我们的 [Bootstrap 教程](https://www.w3schools.com/bootstrap4/)。
Bootstrap 帮助您开发在任何尺寸都外观出众的站点：显示器、笔记本电脑、平板电脑或手机：
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" 
  href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
</head>

<body>

<div class="container">
<div class="jumbotron">
  <h1>W3School Demo</h1> 
  <p>Resize this responsive page!</p> 
</div>
</div>

<div class="container">
<div class="row">
  <div class="col-md-4">
    <h2>London</h2>
    <p>London is the capital city of England.</p>
    <p>It is the most populous city in the United Kingdom,
    with a metropolitan area of over 13 million inhabitants.</p>
  </div>
  <div class="col-md-4">
    <h2>Paris</h2>
    <p>Paris is the capital and most populous city of France.</p>
  </div>
  <div class="col-md-4">
    <h2>Tokyo</h2>
    <p>Tokyo is the capital of Japan, the center of the Greater Tokyo Area,
    and the most populous metropolitan area in the world.</p>
  </div>
</div>
</div>

</body>
</html>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117110326.png" alt="使用现成的 CSS 框架Bootstrap"  title="20200117110326" width="600" height="" /></center>

# HTML 框架

通过使用框架，你可以在同一个浏览器窗口中显示不止一个页面。每份HTML文档称为一个框架，并且每个框架都独立于其他的框架。

使用框架的坏处：
- 开发人员必须同时跟踪更多的HTML文档
- 很难打印整张页面

## 框架结构标签（`<frameset>`）

- 框架结构标签（`<frameset>`）定义如何将窗口分割为框架
- 每个 frameset 定义了一系列行或列
- rows/columns 的值规定了每行或每列占据屏幕的面积
> 编者注：frameset 标签也被某些文章和书籍译为框架集。

## 框架标签（Frame）

Frame 标签定义了放置在每个框架中的 HTML 文档。

在下面的这个例子中，我们设置了一个两列的框架集。第一列被设置为占据浏览器窗口的 25%。第二列被设置为占据浏览器窗口的 75%。HTML 文档 "frame_a.htm" 被置于第一个列中，而 HTML 文档 "frame_b.htm" 被置于第二个列中：
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117111721.png" alt="20200117111721"  title="框架标签Frame" width="600" height="" /></center>

## 基本的注意事项 - 有用的提示：

假如一个框架有可见边框，用户可以拖动边框来改变它的大小。为了避免这种情况发生，可以在 `<frame>` 标签中加入：`noresize="noresize"`。

为不支持框架的浏览器添加 `<noframes>` 标签。

重要提示：不能将 `<body></body>` 标签与 `<frameset></frameset>` 标签同时使用！不过，假如你添加包含一段文本的 `<noframes>` 标签，就必须将这段文字嵌套于 `<body></body>` 标签内。（在下面的第一个实例中，可以查看它是如何实现的。）

## 使用三份不同的文档制作一个垂直框架

可拖动边框调整各个框架的尺寸
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117112434.png" alt="20200117112434"  title="三份不同的文档制作一个垂直框架" width="600" height="" /></center>

## 使用三份不同的文档制作一个水平框架

可拖动边框调整各个框架的尺寸
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117112551.png" alt="20200117112551"  title="20200117112551" width="600" height="" /></center>

## 混合框架结构

可拖动边框调整各个框架的尺寸
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117113207.png" alt="20200117113207"  title="混合框架结构" width="600" height="" /></center>

## 含有 noresize="noresize" 属性的框架结构

 noresize 属性为"noresize"的框架是不可调整尺寸的。在框架间的边框上拖动鼠标，你会发现边框是无法移动的。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117113658.png" alt="20200117113658"  title="20200117113658" width="600" height="" /></center>

## 制作导航框架

导航框架包含一个将第二个框架作为目标的链接列表。名为 "contents.htm" 的文件包含三个链接

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117112900.png" alt="20200117112900"  title="20200117112900" width="600" height="" /></center>

## 内联框架

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117114130.png" alt="20200117114130"  title="20200117114130" width="600" height="" /></center>

## 跳转至框架内的一个指定的节

两个框架。左侧的导航框架包含了一个链接列表，这些链接将第二个框架作为目标。第二个框架显示被链接的文档。导航框架其中的链接指向目标文件中指定的节。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117143904.png" alt="跳转至框架内的一个指定的节"  title="20200117143904" width="600" height="" /></center>

# HTML Iframe

> 参考
[HTML Iframe Tag Generator - 𝗧𝗛𝗘 𝗕𝗘𝗦𝗧 𝗛𝗧𝗠𝗟 𝗖𝗢𝗗𝗘 𝗪𝗜𝗭𝗔𝗥𝗗](https://html-css-js.com/html/generator/iframe/)

<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119211901.png" alt="20200119211901"  title="HTML Iframe Tag Generator" width="600" height="" /><figcaption><font color=green>HTML Iframe Tag Generator</font></figcaption></center></figure>

iframe 用于在网页内显示网页。

## 添加 iframe 的语法

`<iframe src="URL"></iframe>`URL 指向隔离页面的位置。

## Iframe - 设置高度和宽度

height 和 width 属性用于规定 iframe 的高度和宽度。

属性值的默认单位是像素，但也可以用百分比来设定（比如 "80%"）。

`[<iframe src="https://www.w3school.com.cn/html/html_iframe.asp" width=100% height=40%></iframe>](https://youtu.be/j0UMew_Priw)`

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117150629.png" alt="20200117150629"  title="Iframe-设置高度和宽度" width="600" height="" /></center>

## Iframe - 删除边框

frameborder 属性规定是否显示 iframe 周围的边框。

设置属性值为 "0" 就可以移除边框：

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117151023.png" alt="20200117151023"  title="Iframe-删除边框" width="600" height="" /></center>

## 使用 iframe 作为链接的目标

iframe 可用作链接的目标（target）。

链接的 target 属性必须引用 iframe 的 name 属性：
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117151642.png" alt="20200117151642"  title="iframe作为链接的目标" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117152158.png" alt="20200117152158"  title="HTML iframe 标签" width="600" height="" /></center>

## HTML iframe嵌入youtube视频

[嵌入视频和播放列表 - YouTube帮助](https://support.google.com/youtube/answer/171780?hl=zh-Hans)

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200118203901.png" alt="20200118203901"  title="HTML iframe嵌入 youtube 视频方法" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200118204218.png" alt="20200118204218"  title="HTML iframe嵌入 youtube 视频方法" width="600" height="" /></center>

```html
<iframe 
width="560" height="315" 
src="https://www.youtube.com/embed/I31v-HQ9oGo" 
frameborder="0" 
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen>
</iframe>
```

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200118203535.png" alt="20200118203535"  title="HTML iframe嵌入youtube视频" width="600" height="" /></center>


# HTML 背景

## 背景（Backgrounds）

`<body>` 拥有两个配置背景的标签。背景可以是颜色或者图像。
背景属性将背景设置为图像。属性值为图像的URL。如果图像尺寸小于浏览器窗口，那么图像将在整个浏览器窗口进行复制。
```html
<body background="clouds.gif">
<body background="http://www.w3school.com.cn/clouds.gif">
<!-- URL可以是相对地址，如第一行代码。也可以使绝对地址，如第二行代码。 -->
```
> 提示：如果你打算使用背景图片，你需要紧记一下几点：
> - 背景图像是否增加了页面的加载时间。小贴士：图像文件不应超过 10k。
> - 背景图像是否与页面中的其他图象搭配良好。
> - 背景图像是否与页面中的文字颜色搭配良好。
> - 图像在页面中平铺后，看上去还可以吗？
> - 对文字的注意力被背景图像喧宾夺主了吗？

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117153017.png" alt="20200117153017"  title="可用性强的背景图像" width="600" height="" /></center>

## 背景颜色（Bgcolor）

背景颜色属性将背景设置为某种颜色。属性值可以是十六进制数、RGB 值或颜色名。
```html
<body bgcolor="#000000">
<body bgcolor="rgb(0,0,0)">
<body bgcolor="black">
<!-- 以上的代码均将背景颜色设置为黑色。 -->
```

## 基本的注意事项 - 有用的提示：

`<body>` <font color=red>标签中的背景颜色（bgcolor）、背景（background）和文本（text）属性在最新的 HTML 标准（HTML4 和 XHTML）中已被废弃</font>。W3C 在他们的推荐标准中已删除这些属性。

应该使用<font color=blue>层叠样式表（CSS）来定义 HTML 元素的布局和显示属性</font>。

# HTML 脚本

JavaScript 使 HTML 页面具有更强的动态和交互性。。

## HTML script 元素

`<script>` 标签用于定义客户端脚本，比如 JavaScript。
script 元素既可包含脚本语句，也可通过 src 属性指向外部脚本文件。
必需的 type 属性规定脚本的 MIME 类型。
JavaScript 最常用于图片操作、表单验证以及内容动态更新。

下面的脚本会向浏览器输出“Hello World!”：
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117153425.png" alt="20200117153425"  title="脚本会向浏览器输出Hello World!" width="600" height="" /></center>

> 提示：如果需要学习更多有关在 HTML 中编写脚本的知识，请访问我们的 [JavaScript 教程](https://www.w3school.com.cn/js/index.asp)。

## `<noscript>` 标签

`<noscript>` 标签提供无法使用脚本时的替代内容，比方在浏览器禁用脚本时，或浏览器不支持客户端脚本时。

noscript 元素可包含普通 HTML 页面的 body 元素中能够找到的所有元素。

只有在浏览器不支持脚本或者禁用脚本时，才会显示 noscript 元素中的内容：
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117153810.png" alt="20200117153810"  title="noscript 元素中的内容" width="600" height="" /></center>

## 如何应付老式的浏览器

如果浏览器压根没法识别 `<script>` 标签，那么 `<script>` 标签所包含的内容将以文本方式显示在页面上。为了避免这种情况发生，你应该将脚本隐藏在注释标签当中。那些老的浏览器（无法识别 `<script>` 标签的浏览器）将忽略这些注释，所以不会将标签的内容显示到页面上。而那些新的浏览器将读懂这些脚本并执行它们，即使代码被嵌套在注释标签内。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117154336.png" alt="20200117154336"  title="识别 script标签的浏览器将显示这些注释-无法识别 script标签的浏览器将忽略这些注释" width="600" height="" /></center>

| 标签         | 描述                                     |
| ------------ | ---------------------------------------- |
| `<script>`   | 定义客户端脚本。                         |
| `<noscript>` | 为不支持客户端脚本的浏览器定义替代内容。 |

## HTML 文件路径

文件路径描述了网站文件夹结构中某个文件的位置。

文件路径会在链接外部文件时被用到：
- 网页
- 图像
- 样式表
- JavaScript

| 路径                              | 描述                                         |
| --------------------------------- | -------------------------------------------- |
| `<img src="picture.jpg">`         | picture.jpg 位于与当前网页相同的文件夹       |
| `<img src="images/picture.jpg">`  | picture.jpg 位于当前文件夹的 images 文件夹中 |
| `<img src="/images/picture.jpg">` | picture.jpg 当前站点根目录的 images 文件夹中 |
| `<img src="../picture.jpg">`      | picture.jpg 位于当前文件夹的上一级文件夹中   |

## 绝对文件路径

绝对文件路径是指向一个因特网文件的完整 URL：
`<img src="https://www.w3school.com.cn/images/picture.jpg" alt="flower">`

## 相对路径

相对路径指向了相对于当前页面的文件。

在本例中，文件路径指向了位于当前网站根目录中 images 文件夹里的一个文件：
`<img src="/images/picture.jpg" alt="flower">`

## 好习惯

使用相对路径是个好习惯（如果可能）。

如果使用了相对路径，那么您的网页就不会与当前的基准 URL 进行绑定。所有链接在您的电脑上 (localhost) 或未来的公共域中均可正常工作。

# HTML 头部元素

## HTML `<head>` 元素

`<head>` 元素是所有头部元素的容器。`<head>` 内的元素可包含脚本，指示浏览器在何处可以找到样式表，提供元信息，等等。

以下标签都可以添加到 head 部分：`<title>、<base>、<link>、<meta>、<script> 以及 <style>`。

## HTML `<title>` 元素

`<title>` 标签定义文档的标题。

title 元素在所有 HTML/XHTML 文档中都是必需的。

title 元素能够： 
- 定义浏览器工具栏中的标题
- 提供页面被添加到收藏夹时显示的标题
- 显示在搜索引擎结果中的页面标题

一个简化的 HTML 文档：
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117171735.png" alt="20200117171735"  title="head标签里的title标签定义文档的网页标题" width="600" height="" /></center>

## HTML `<base>` 元素

`<base>` 标签为页面上的所有链接规定默认地址或默认目标（target）：
```html
<head>
<base href="http://www.w3school.com.cn/images/" />
<base target="_blank" />
</head>
```

## HTML `<link>` 元素

> 参考
[HTML Link Tag Generator - 𝗧𝗛𝗘 𝗕𝗘𝗦𝗧 𝗛𝗧𝗠𝗟 𝗖𝗢𝗗𝗘 𝗪𝗜𝗭𝗔𝗥𝗗](https://html-css-js.com/html/generator/link/)

<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119212343.png" alt="20200119212343"  title="HTML Link Tag Generator" width="600" height="" /><figcaption><font color=green>HTML Link Tag Generator</font></figcaption></center></figure>

`<link>` 标签定义文档与外部资源之间的关系。

`<link>` 标签最常用于连接样式表：
```html
<head>
<link rel="stylesheet" type="text/css" href="mystyle.css" />
</head>
```

## HTML `<style>` 元素

`<style>` 标签用于为 HTML 文档定义样式信息。

您可以在 style 元素内规定 HTML 元素在浏览器中呈现的样式：
```html
<head>
<style type="text/css">
body {background-color:yellow}
p {color:blue}
</style>
</head>
```

## HTML `<meta>` 元素

元数据（metadata）是关于数据的信息。

- `<meta>` 标签提供关于 HTML 文档的元数据。元数据不会显示在页面上，但是对于机器是可读的。
- 典型的情况是，meta 元素被用于规定页面的描述、关键词、文档的作者、最后修改时间以及其他元数据。
- `<meta>` 标签始终位于 head 元素中。
- 元数据可用于浏览器（如何显示内容或重新加载页面），搜索引擎（关键词），或其他 web 服务。

### 针对搜索引擎的关键词

一些搜索引擎会利用 meta 元素的 name 和 content 属性来索引您的页面。

下面的 meta 元素定义页面的描述：
`<meta name="description" content="Free Web tutorials on HTML, CSS, XML" />`

下面的 meta 元素定义页面的关键词：
`<meta name="keywords" content="HTML, CSS, XML" />`

name 和 content 属性的作用是描述页面的内容。

## HTML `<script>` 元素

`<script>` 标签用于定义客户端脚本，比如 JavaScript。

## HTML 头部元素

| 标签       | 描述                                     |
| ---------- | ---------------------------------------- |
| `<head>`   | 定义关于文档的信息。                     |
| `<title>`  | 定义文档标题。                           |
| `<base>`   | 定义页面上所有链接的默认地址或默认目标。 |
| `<link>`   | 定义文档与外部资源之间的关系。           |
| `<meta>`   | 定义关于 HTML 文档的元数据。             |
| `<script>` | 定义客户端脚本。                         |
| `<style>`  | 定义文档的样式信息。                     |

# HTML 实体

HTML 中的预留字符必须被替换为字符实体。
如需完整的实体符号参考，请访问我们的 [HTML 实体符号参考手册](https://www.w3school.com.cn/tags/html_ref_entities.html)。

##  HTML 字符实体

- 在 HTML 中，某些字符是预留的。
- 在 HTML 中不能使用小于号（<）和大于号（>），这是因为浏览器会误认为它们是标签。
- 如果希望正确地显示预留字符，我们必须在 HTML 源代码中使用字符实体（character entities）。

字符实体类似这样：
```html
&entity_name;

或者

&#entity_number;
```
> 如需显示小于号，我们必须这样写：`&lt;` 或 `&#60;`
提示：使用实体名而不是数字的好处是，名称易于记忆。不过坏处是，浏览器也许并不支持所有实体名称（对实体数字的支持却很好）。

## 不间断空格（non-breaking space）

HTML 中的常用字符实体是不间断空格(`&nbsp;`)。

浏览器总是会截短 HTML 页面中的空格。如果您在文本中写 10 个空格，在显示该页面之前，浏览器会删除它们中的 9 个。如需在页面中增加空格的数量，您需要使用 `&nbsp; `字符实体。

## HTML 实例示例

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117174040.png" alt="20200117174040"  title="HTML 实体" width="600" height="" /></center>

## HTML 中有用的字符实体

> 注释：实体名称对大小写敏感！

| 显示结果 | 描述              | 实体名称             | 实体编号   |
| -------- | ----------------- | -------------------- | ---------- |
|          | 空格              | `&nbsp;`             | ` &#160;`  |
| `<`      | 小于号            | `&lt; `              | `&#60`     |
| $>$      | 大于号            | `&gt; `              | `&#62;`    |
| &        | 和号              | `&amp;`              | `&#38;`    |
| "        | 引号              | `&quot;`             | `&#34;`    |
| '        | 撇号              | ` &apos;` (IE不支持) | `&#39;`    |
| ￠        | 分（cent）        | `&cent; `            | `&#162; `  |
| £        | 镑（pound）       | `&pound;`            | `&#163;`   |
| ¥        | 元（yen）         | `&yen; `             | `&#165;`   |
| €        | 欧元（euro）      | ` &euro; `           | `&#8364;`  |
| §        | 小节              | `&sect;`             | `&#167; `  |
| ©        | 版权（copyright） | `&copy;`             | `&#169;`   |
| ®        | 注册商标          | `&reg; `             | ` &#174; ` |
| ™        | 商标              | `&trade; `           | `&#8482;`  |
| ×        | 乘号              | `&times; `           | `&#215;`   |
| ÷        | 除号              | `&divide;`           | `&#247; `  |

# HTML 统一资源定位器

URL 也被称为网址。

URL 可以由单词组成，比如 “w3school.com.cn”，或者是因特网协议（IP）地址：192.168.1.253。大多数人在网上冲浪时，会键入网址的域名，因为名称比数字容易记忆。

## URL - Uniform Resource Locator

当您点击 HTML 页面中的某个链接时，对应的 <a> 标签指向万维网上的一个地址。

统一资源定位器（URL）用于定位万维网上的文档（或其他数据）。

网址，比如 http://www.w3school.com.cn/html/index.asp，遵守以下的语法规则：
`scheme://host.domain:port/path/filename`
解释：
- scheme - 定义因特网服务的类型。最常见的类型是 http
- host - 定义域主机（http 的默认主机是 www）
- domain - 定义因特网域名，比如 w3school.com.cn
- :port - 定义主机上的端口号（http 的默认端口号是 80）
- path - 定义服务器上的路径（如果省略，则文档必须位于网站的根目录中）。
- filename - 定义文档/资源的名称

> 编者注：URL 的英文全称是 Uniform Resource Locator，中文也译为“统一资源定位符”。

## URL Schemes

以下是其中一些最流行的 scheme：

| Scheme | 访问               | 用于...                             |
| ------ | ------------------ | ----------------------------------- |
| http   | 超文本传输协议     | 以 http:// 开头的普通网页。不加密。 |
| https  | 安全超文本传输协议 | 安全网页。加密所有信息交换。        |
| ftp    | 文件传输协议       | 用于将文件下载或上传至网站。        |
| file   | -                  | 您计算机上的文件。                  |

## HTML URL 字符编码

URL 编码会将字符转换为可通过因特网传输的格式

## URL - 统一资源定位器

Web 浏览器通过 URL 从 web 服务器请求页面。

URL 是网页的地址，比如 <http://www.w3school.com.cn>

## URL  编码

如需完整的 URL 编码参考，请访问我们的 [URL 编码参考手册](https://www.w3school.com.cn/tags/html_ref_urlencode.html)。
URL 只能使用 ASCII 字符集来通过因特网进行发送。
由于 URL 常常会包含 ASCII 集合之外的字符，URL 必须转换为有效的 ASCII 格式。
URL 编码使用 "%" 其后跟随两位的十六进制数来替换非 ASCII 字符。
URL 不能包含空格。URL 编码通常使用 + 来替换空格。
[亲自试一试-URL  编码](https://www.w3school.com.cn/html/html_urlencode.asp)
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117185008.png" alt="20200117185008"  title="URL  编码" width="600" height="" /></center>

## URL 编码示例

| 字符 | URL 编码 |
|------|----------|
| €    | %80      |
| £    | %A3      |
| ©    | %A9      |
| ®    | %AE      |
| À    | %C0      |
| Á    | %C1      |
| Â    | %C2      |
| Ã    | %C3      |
| Ä    | %C4      |
| Å    | %C5      |

# HTML Web Server

如果希望向世界发布您的网站，那么您必须把它存放在 web 服务器上。

## 托管自己的网站

在自己的服务器上托管网站始终是一个选项。有几点需要考虑：
硬- 件支出
如果要运行“真正”的网站，您不得不购买强大的服务器硬件。不要指望低价的 PC 能够应付这些工作。您还需要稳定的（一天 24 小时）高速连接。
- 软件支出
请记住，服务器授权通常比客户端授权更昂贵。同时请注意，服务器授权也许有用户数量限制。
- 人工费
不要指望低廉的人工费用。您必须安装自己的硬件和软件。您同时要处理漏洞和病毒，以确保您的服务器时刻正常地运行于一个“任何事都可能发生”的环境中。

## 使用因特网服务提供商（ISP）

从 ISP 租用服务器也很常见。

大多数小公司会把网站存放到由 ISP 提供的服务器上。其优势有以下几点：
- 连接速度
大多数 ISP 都拥有连接因特网的高速连接。
- 强大的硬件
ISP 的 web 服务器通常强大到能够由若干网站分享资源。您还要看一下 ISP 是否提供高效的负载平衡，以及必要的备份服务器。
- 安全性和可靠性
ISP 是网站托管方面的专家。他们应该提供 99% 以上的在线时间，最新的软件补丁，以及最好的病毒防护。

## 选择 ISP 时的注意事项

- 24 小时支持
确保 ISP 提供 24 小时支持。不要使自己置于无法解决严重问题的尴尬境地，同时还必须等待第二个工作日。如果您不希望支付长途电话费，那么免费电话服务也是必要的。
- 每日备份
确保 ISP 会执行每日备份的例行工作，否则您有可能损失有价值的数据。
- 流量
研究一下 ISP 的流量限制。如果出现由于网站受欢迎而激增的不可预期的访问量，那么您要确保不会因此支付额外费用。
- 带宽或内容限制
研究一下 ISP 的带宽和内容限制。如果您计划发布图片或播出视频或音频，请确保您有此权限。
- E-mail 功能
请确保 ISP 支持您需要的 e-mail 功能。
- 数据库访问
如果您计划使用网站数据库中的数据，那么请确保您的 ISP 支持您需要的数据库访问。

在您选取一家 ISP 之前，请务必阅读 W3School 的 [Web 主机教程](https://www.w3school.com.cn/hosting/index.asp)。

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200118111331.png" alt="20200118111331"  title="网站主机教程" width="600" height="" /></center>

# HTML 颜色

颜色由三元色：红色、绿色、蓝色混合而成。

## 颜色值

颜色由一个十六进制符号来定义，这个符号由红色、绿色和蓝色的值组成（RGB）。
每种颜色的最小值是0（十六进制：#00）。最大值是255（十六进制：#FF）。
这个表格给出了由三种颜色混合而成的具体效果：

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200118111756.png" alt="20200118111756"  title="颜色值" width="600" height="" /></center>

## 颜色名

大多数的浏览器都支持颜色名集合。

提示：仅仅有 16 种颜色名被 W3C 的 HTML4.0 标准所支持。它们是：aqua, black, blue, fuchsia, gray, green, lime, maroon, navy, olive, purple, red, silver, teal, white, yellow。

如果需要使用其它的颜色，需要使用十六进制的颜色值。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200118111923.png" alt="20200118111923"  title="除16 种颜色外的其它颜色需要使用十六进制的颜色值" width="600" height="" /></center>

## Web安全色

数年以前，当大多数计算机仅支持 256 种颜色的时候，一系列 216 种 Web 安全色作为 Web 标准被建议使用。其中的原因是，微软和 Mac 操作系统使用了 40 种不同的保留的固定系统颜色（双方大约各使用 20 种）。

我们不确定如今这么做的意义有多大，因为越来越多的计算机有能力处理数百万种颜色，不过做选择还是你自己。

## 216 跨平台色

最初，216 跨平台 web 安全色被用来确保：当计算机使用 256 色调色板时，所有的计算机能够正确地显示所有的颜色。

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200118112239.png" alt="20200118112239"  title="216 跨平台色" width="600" height="" /></center>

# HTML 颜色名

本页提供了被大多数浏览器支持的颜色名。

提示：仅有 16 种颜色名被 W3C 的 HTML 4.0 标准支持，它们是：aqua、black、blue、fuchsia、gray、green、lime、maroon、navy、olive、purple、red、silver、teal、white、yellow。

如果使用其它颜色的话，就应该使用十六进制的颜色值。

## 颜色名列表

单击一个颜色名或者 16 进制值，就可以查看与不同文字颜色搭配的背景颜色。

[颜色名列表](https://www.w3school.com.cn/html/html_colornames.asp)
[W3School 颜色测试](https://www.w3school.com.cn/tiy/color.asp?hex=F0F8FF)

# HTML文档类型

## HTML `<!DOCTYPE>`

`<!DOCTYPE>` 声明帮助浏览器正确地显示网页。

## `<!DOCTYPE>` 声明

Web 世界中存在许多不同的文档。只有了解文档的类型，浏览器才能正确地显示文档。

HTML 也有多个不同的版本，只有完全明白页面中使用的确切 HTML 版本，浏览器才能完全正确地显示出 HTML 页面。这就是 <!DOCTYPE> 的用处。

`<!DOCTYPE>` 不是 HTML 标签。它为浏览器提供一项信息（声明），即 HTML 是用什么版本编写的。

提示：W3School 即将升级为最新的 HTML5 文档类型。

带有 HTML5 DOCTYPE 的 HTML 文档：

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200117171735.png" alt="20200117171735"  title="带有 HTML5 DOCTYPE 的 HTML 文档" width="600" height="" /></center>

## HTML 版本

从 Web 诞生早期至今，已经发展出多个 HTML 版本：

| 版本      | 年份 |
|-----------|------|
| HTML      | 1991 |
| HTML+     | 1993 |
| HTML 2.0  | 1995 |
| HTML 3.2  | 1997 |
| HTML 4.01 | 1999 |
| XHTML 1.0 | 2000 |
| HTML5     | 2012 |
| XHTML5    | 2013 |

## 常用的声明

如需完整的文档类型声明列表，请访问我们的 [DOCTYPE 参考手册](https://www.w3school.com.cn/tags/tag_doctype.asp)。
### HTML5

`<!DOCTYPE html>`

### HTML 4.01

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
```

### XHTML 1.0

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
```

# HTML 4.01 快速参考

来自 W3School 的 [HTML 快速参考](http://www.w3school.com.cn/html/html_quick.asp)。可以打印它，以备日常使用。

## HTML Basic Document

```html
<html>
<head>
<title>Document name goes here</title>
</head>
<body>
Visible text goes here
</body>
</html>
```

## Text Elements

```html
<p>This is a paragraph</p>
<br> (line break)
<hr> (horizontal rule)
<pre>This text is preformatted</pre>
```

## Logical Styles

```html
<em>This text is emphasized</em>
<strong>This text is strong</strong>
<code>This is some computer code</code>
```

## Physical Styles

```html
<b>This text is bold</b>
<i>This text is italic</i>
```

## Links, Anchors, and Image Elements

```html
<a href="http://www.example.com/">This is a Link</a>
<a href="http://www.example.com/"><img src="URL"
alt="Alternate Text"></a>
<a href="mailto:webmaster@example.com">Send e-mail</a>A named anchor:
<a name="tips">Useful Tips Section</a>
<a href="#tips">Jump to the Useful Tips Section</a>
```

## Unordered list

```html
<ul>
<li>First item</li>
<li>Next item</li>
</ul>
```

## Ordered list

```html
<ol>
<li>First item</li>
<li>Next item</li>
</ol>
```

## Definition list

```html
<dl>
<dt>First term</dt>
<dd>Definition</dd>
<dt>Next term</dt>
<dd>Definition</dd>
</dl>
```

## Tables

```html
<table border="1">
<tr>
  <th>someheader</th>
  <th>someheader</th>
</tr>
<tr>
  <td>sometext</td>
  <td>sometext</td>
</tr>
</table>
```

## Frames 框架

```html
<!-- 水平排列 -->
<frameset rows="25%,*,35%">
  <frame src="page1.htm">
  <frame src="page2.htm">
    <frame src="page3.htm">
</frameset>

<!-- 竖直排列 -->
<frameset cols="25%,*,35%">
  <frame src="page1.htm">
  <frame src="page2.htm">
    <frame src="page3.htm">
</frameset>
```

## Forms 表单

> 参考
[HTML Form Tag Generator - 𝗧𝗛𝗘 𝗕𝗘𝗦𝗧 𝗛𝗧𝗠𝗟 𝗖𝗢𝗗𝗘 𝗪𝗜𝗭𝗔𝗥𝗗](https://html-css-js.com/html/generator/form/)

<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119213259.png" alt="20200119213259"  title="HTML Form Tag Generator" width="600" height="" /><figcaption><font color=green>HTML Form Tag Generator</font></figcaption></center></figure>

```html
<form action="http://www.example.com/test.asp" method="post/get">
<input type="text" name="lastname"
value="Nixon" size="30" maxlength="50">
<input type="password">
<input type="checkbox" checked="checked">
<input type="radio" checked="checked">
<input type="submit">
<input type="reset">
<input type="hidden">
<select>
<option>Apples
<option selected>Bananas
<option>Cherries
</select>
<textarea name="Comment" rows="60"
cols="20"></textarea>
</form>
```

## Entities

```html
&lt; is the same as <
&gt; is the same as >
&#169; is the same as ©
```

## Other Elements

```html
<!-- This is a comment -->
<blockquote>
Text quoted from some source.
</blockquote>
<address>
Address 1<br>
Address 2<br>
City<br>
</address>
```

# HTML 实例

<a href="https://www.w3school.com.cn/example/html_examples.asp">HTML 实例</a>

## HTML 基础标签实例

### 一个简单的 HTML 文件

一个很简单的 HTML 文件，使用了尽可能少的 HTML 标签。它向您演示了 body 元素中的内容是如何被浏览器显示的。

```html
<html>

<head>
<title>我的第一个 HTML 页面</title>
</head>

<body>
<p>body 元素的内容会显示在浏览器中。</p>
<p>title 元素的内容会显示在浏览器的标题栏中。</p>
</body>

</html>
```

### 简单的段落

段落元素中的文字如何被浏览器显示。
```html
<html>
<body>

<p>这是段落。</p>
<p>这是段落。</p>
<p>这是段落。</p>

<p>段落元素由 p 标签定义。</p> 

</body>
</html>
```

### 更多的段落

段落元素的某些缺省的行为
```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">

<html>

<body>

<p>
这个段落
在源代码中
包含许多行
但是浏览器
忽略了它们。只保留一个空格
</p>

<p>
这个段落
在源代码       中
包含   许多行
但是      浏览器
忽略了  它们。只保留一个空格
</p>

<p>
段落的行数依赖于浏览器窗口的大小。如果调节浏览器窗口的大小，将改变段落中的行数。
</p>

</body>
</html>
```

### “诗歌”问题

演示 HTML 格式化的某些问题。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119114304.png" alt="20200119114304"  title="HTML 格式化的某些问题" width="600" height="" /><figcaption><font color=green>HTML 格式化的某些问题</font></figcaption></center></figure>

### 折行

在 HTML 文档中折行的使用
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119114754.png" alt="20200119114754"  title="在 HTML 文档中折行的使用" width="600" height="" /><figcaption><font color=green>在 HTML 文档中折行的使用</font></figcaption></center></figure>

### 标题

在 HTML 文档中显示标题的标签
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119114928.png" alt="20200119114928"  title="标题的标签" width="600" height="" /><figcaption><font color=green>标题的标签</font></figcaption></center></figure>

### 居中排列的标题

一个居中排列的标题
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119115258.png" alt="20200119115258"  title="居中排列的标题" width="600" height="" /><figcaption><font color=green>居中排列的标题</font></figcaption></center></figure>

### 水平线

如何插入水平线
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119115444.png" alt="20200119115444"  title="插入水平线" width="600" height="" /><figcaption><font color=green>插入水平线</font></figcaption></center></figure>

### 隐藏的注释

本例演示如何在 HTML 源代码中插入隐藏的注释。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119115612.png" alt="20200119115612"  title="插入隐藏的注释" width="600" height="" /><figcaption><font color=green>插入隐藏的注释</font></figcaption></center></figure>

### 背景颜色

本例演示如何为 HTML 页面添加背景颜色。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119115815.png" alt="20200119115815"  title="添加背景颜色" width="600" height="" /><figcaption><font color=green>添加背景颜色</font></figcaption></center></figure>

## HTML 文本格式化实例

### 文本格式化

此例演示如何在一个 HTML 文件中对文本进行格式化
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119120047.png" alt="20200119120047"  title="文本格式化" width="600" height="" /><figcaption><font color=green>文本格式化</font></figcaption></center></figure>

### 预格式文本pre

此例演示如何使用 pre 标签对空行和空格进行控制。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119120230.png" alt="20200119120230"  title="预格式文本pre" width="600" height="" /><figcaption><font color=green>预格式文本pre</font></figcaption></center></figure>

### “计算机输出”标签

此例演示不同的“计算机输出”标签的显示效果。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119120507.png" alt="20200119120507"  title="计算机输出标签" width="600" height="" /><figcaption><font color=green>计算机输出标签</font></figcaption></center></figure>

### 地址address

此例演示如何在 HTML 文件中写地址。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119120714.png" alt="20200119120714"  title="地址address" width="600" height="" /><figcaption><font color=green>地址address</font></figcaption></center></figure>

### 缩写和首字母缩写

此例演示如何实现缩写或首字母缩写。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119153157.png" alt="20200119153157"  title="abbreviation缩写词acronym首字母缩略词" width="600" height="" /><figcaption><font color=green>abbreviation缩写词acronym首字母缩略词</font></figcaption></center></figure>

### 文字方向bdo

此例演示如何改变文字的方向。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119153508.png" alt="20200119153508"  title="改变文字的方向bdo" width="600" height="" /><figcaption><font color=green>改变文字的方向bdo</font></figcaption></center></figure>

### 块引用blockquote or q

此例演示如何实现长短不一的引用语。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119153845.png" alt="20200119153845"  title="块引用blockquote or q" width="600" height="" /><figcaption><font color=green>块引用blockquote or q</font></figcaption></center></figure>

### 删除del字效果和插入ins字效果

此例演示如何标记删除文本和插入文本。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119154221.png" alt="20200119154221"  title="删除del字效果和插入ins字效果" width="600" height="" /><figcaption><font color=green>删除del字效果和插入ins字效果</font></figcaption></center></figure>

## HTML 链接实例

### 创建超级链接a-href

本例演示如何在 HTML 文档中创建链接。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119154534.png" alt="20200119154534"  title="创建超级链接a-href" width="600" height="" /><figcaption><font color=green>创建超级链接a-href</font></figcaption></center></figure>

### 将图像作为链接a_href-img

本例演示如何使用图像作为链接。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119154928.png" alt="20200119154928"  title="将图像作为链接a_href-img" width="600" height="" /><figcaption><font color=green>将图像作为链接a_href-img</font></figcaption></center></figure>

### 在新的浏览器窗口打开链接a_href_target

本例演示如何在新窗口打开一个页面，这样的话访问者就无需离开你的站点了。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119155210.png" alt="20200119155210"  title="在新的浏览器窗口打开链接a_href_target" width="600" height="" /><figcaption><font color=green>在新的浏览器窗口打开链接a_href_target</font></figcaption></center></figure>

### 跳出框架a_href_target

本例演示如何跳出框架，假如你的页面被固定在框架之内。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119155548.png" alt="20200119155548"  title="跳出框架a_href_target" width="600" height="" /><figcaption><font color=green>跳出框架a_href_target</font></figcaption></center></figure>

### 创建电子邮件链接a_href_subject_body

本例演示如何如何链接到一个邮件。（本例在安装邮件客户端程序后才能工作。）
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119160050.png" alt="20200119160050"  title="创建电子邮件链接a_href" width="600" height="" /><figcaption><font color=green>创建电子邮件链接a_href</font></figcaption></center></figure>

<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119160633.png" alt="20200119160633"  title="创建电子邮件链接a_href_subject_body" width="600" height="" /><figcaption><font color=green>创建电子邮件链接a_href_subject_body</font></figcaption></center></figure>

## HTML 框架实例

### 垂直框架frameset_cols

本例演示：如何使用三份不同的文档制作一个垂直框架。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119161101.png" alt="20200119161101"  title="垂直框架frameset_cols" width="600" height="" /><figcaption><font color=green>垂直框架frameset_cols</font></figcaption></center></figure>

### 水平框架frameset_rows

本例演示：如何使用三份不同的文档制作一个水平框架。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119161408.png" alt="20200119161408"  title="水平框架frameset_rows" width="600" height="" /><figcaption><font color=green>水平框架frameset_rows</font></figcaption></center></figure>

### 如何使用 `<noframes>` 标签

本例演示：如何使用 `<noframes>` 标签。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119161809.png" alt="20200119161809"  title="noframes标签" width="600" height="" /><figcaption><font color=green>noframes标签</font></figcaption></center></figure>

### 混合框架结构frameset_rows_cols

本例演示如何制作含有三份文档的框架结构，同时将他们混合置于行和列之中。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119162354.png" alt="20200119162354"  title="" width="600" height="" /><figcaption><font color=green></font></figcaption></center></figure>

### 含有 noresize="noresize" 属性的框架结构

本例演示 noresize 属性。在本例中，框架是不可调整尺寸的。在框架间的边框上拖动鼠标，你会发现边框是无法移动的。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119163048.png" alt="20200119163048"  title="框架结构frameset_src_noresize" width="600" height="" /><figcaption><font color=green>框架结构frameset_src_noresize</font></figcaption></center></figure>

### 导航框架

本例演示如何制作导航框架。导航框架包含一个将第二个框架作为目标的链接列表。名为 "contents.htm" 的文件包含三个链接。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119163703.png" alt="20200119163703"  title=" 导航框架frameset_src" width="600" height="" /><figcaption><font color=green> 导航框架frameset_src</font></figcaption></center></figure>

### 内联框架iframe

本例演示如何创建内联框架（HTML 页中的框架）。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119163944.png" alt="20200119163944"  title="内联框架iframe" width="600" height="" /><figcaption><font color=green>内联框架iframe</font></figcaption></center></figure>

### 跳转至框架内的一个指定的节frameset_cols-frame_src

本例演示两个框架。其中的一个框架设置了指向另一个文件内指定的节的链接。这个"link.htm"文件内指定的节使用 `<a name="C10">` 进行标识。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119164335.png" alt="20200119164335"  title="跳转至框架内的一个指定的节frameset_cols-frame_src" width="600" height="" /><figcaption><font color=green>跳转至框架内的一个指定的节frameset_cols-frame_src</font></figcaption></center></figure>

### 使用框架导航跳转至指定的节

本例演示两个框架。左侧的导航框架包含了一个链接列表，这些链接将第二个框架作为目标。第二个框架显示被链接的文档。导航框架其中的链接指向目标文件中指定的节。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200119164810.png" alt="20200119164810"  title="使用框架导航跳转至指定的节" width="600" height="" /><figcaption><font color=green>使用框架导航跳转至指定的节</font></figcaption></center></figure>

## HTML 表格实例

[HTML 实例](https://www.w3school.com.cn/example/html_examples.asp)
