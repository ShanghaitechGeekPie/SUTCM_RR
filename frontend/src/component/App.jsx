import React, { Component } from 'react';
import { DatePicker } from 'antd';
import { Col, Breadcrumb, Icon, Button, Steps, Form, Input, Select } from 'antd';
const FormItem = Form.Item;
const Step = Steps.Step;
const Option = Select.Option;

require("../css/web.css");

class Breadcrumbs extends Component {
	render() {
	return <div id="Breadcrumbs">
			<Breadcrumb>
				<Breadcrumb.Item href="http://www.shutcm.edu.cn/">
					<Icon type="home" />
					首页
				</Breadcrumb.Item>
				<Breadcrumb.Item href="http://www.shutcm.edu.cn/c/portal/layout?p_l_id=PUB.1001.30">
					<Icon type="desktop" />
					公共服务
				</Breadcrumb.Item>
				<Breadcrumb.Item href="">
					<Icon type="book" />
					资源预约
				</Breadcrumb.Item>
				<Breadcrumb.Item>
					应用
				</Breadcrumb.Item>
			</Breadcrumb>
		</div>;
	}
}

class Indexes extends Component {
	render() {
	return <div id="Indexes">
			<h2>请选择操作:</h2>
			<Button type="ghost" size="large">
				<Icon type="pie-chart" />
				<br/>
				教室查询
			</Button>
			<Button type="ghost" size="large">
				<Icon type="home" />
				<br/>
				教室申请
			</Button>
			<br />
			<Button type="ghost" size="large">
				<Icon type="solution" />
				<br/>
				咨询申请
			</Button>
			<Button type="ghost" size="large">
				<Icon type="file-unknown" />
				<br/>
				结果查询
			</Button>
		</div>;
	}
}

class IndexApp extends Component {
	render() {
	return <div className="card">
			<Breadcrumbs />
			<Indexes />
		</div>;
	}
}

class ReserveSteps extends Component {
	render() {
	return <div id="ReserveSteps">
			<Steps>
				<Step status="finish" title="申请对象" icon="share-alt" />
				<Step status="process" title="申请资料" icon="solution" />
				<Step status="wait" title="提交申请" icon="check" />
			</Steps>
		</div>;
	}

}


class ReserveForm extends Component {
	render() {
	return <Form horizontal className="form" >
			<div id="ReserveFormStep1">
				<FormItem
					id="control-name"
					label="姓名："
					labelCol={{ span: 8 }}
					wrapperCol={{ span: 10 }}>
					<Input type="text" placeholder="请输入您的姓名" />
				</FormItem>
				<FormItem
					id="control-phone"
					label="手机号码："
					labelCol={{ span: 8 }}
					wrapperCol={{ span: 10 }}>
					<Input type="text" placeholder="请输入您的手机号码" />
				</FormItem>
				<FormItem
					id="control-department"
					label="学院："
					labelCol={{ span: 8 }}
					wrapperCol={{ span: 10 }}>
					<Select showSearch
						placeholder="请选择学院"
						optionFilterProp="children"
						notFoundContent="无法找到"
						searchPlaceholder="输入关键词">
						<Option value="jack">杰克</Option>
						<Option value="lucy">露西</Option>
						<Option value="tom">汤姆</Option>
					</Select>
				</FormItem>
				<FormItem
					id="control-textarea"
					label="文本域："
					labelCol={{ span: 8 }}
					wrapperCol={{ span: 10 }}>
					<Input type="password" placeholder="请输入密码" />
				</FormItem>
			</div>
			<div id="ReserveFormStep2">
				<FormItem
					id="control-name"
					label="姓名："
					labelCol={{ span: 8 }}
					wrapperCol={{ span: 10 }}>
					<Input type="text" placeholder="请输入您的姓名" />
				</FormItem>
				<FormItem
					id="control-phone"
					label="手机号码："
					labelCol={{ span: 8 }}
					wrapperCol={{ span: 10 }}>
					<Input type="text" placeholder="请输入您的手机号码" />
				</FormItem>
				<FormItem
					id="control-department"
					label="学院："
					labelCol={{ span: 8 }}
					wrapperCol={{ span: 10 }}>
					<Select showSearch
						placeholder="请选择学院"
						optionFilterProp="children"
						notFoundContent="无法找到"
						searchPlaceholder="输入关键词">
						<Option value="jack">杰克</Option>
						<Option value="lucy">露西</Option>
						<Option value="tom">汤姆</Option>
					</Select>
				</FormItem>
				<FormItem
					id="control-purpose"
					label="使用目的："
					labelCol={{ span: 8 }}
					wrapperCol={{ span: 10 }}>
					<Input type="textarea" placeholder="请输入使用目的" rows="3" />
				</FormItem>
				<FormItem
					id="control-purpose"
					label="使用目的："
					labelCol={{ span: 8 }}
					wrapperCol={{ span: 10 }}>
					<Input type="text" placeholder="请输入使用目的" />
				</FormItem>
			</div>
		</Form>;
	}

}

class App extends Component {
	render() {
	return <div className="card">
			<Breadcrumbs />
			<ReserveSteps />
			<ReserveForm />
		</div>;
	}
}

export default App;
// export default IndexApp;
// export default ReserveApp;
// export default ResultApp;

