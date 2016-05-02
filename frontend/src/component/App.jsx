import React, { Component } from 'react';
import { Row, Col, Breadcrumb, Icon, Button, Steps, Form, Input, Select, DatePicker, Alert, Spin } from 'antd';
const FormItem = Form.Item;
const Step = Steps.Step;
const Option = Select.Option;
import { Router, Route, hashHistory, Link } from 'react-router'

require("../css/web.css");

var Breadcrumbs = React.createClass({
	render: function() {
		if (this.props.route.path == "/")
			var Item = "首页"
		else if (this.props.route.path == "/resource")
			var Item = "教室查询"
		else if (this.props.route.path == "/reserve")
			var Item = "教室申请"
		else if (this.props.route.path == "/result")
			var Item = "结果查询";

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
				<Link to="/">
					<Breadcrumb.Item>
						<Icon type="book" />
						资源预约
					</Breadcrumb.Item>
				</Link>
				<Breadcrumb.Item>
					{Item}
				</Breadcrumb.Item>
			</Breadcrumb>
		</div>;
	}
});

var IndexApp = React.createClass({
	render: function() {
		return <div id="Indexes">
			<h2>请选择操作:</h2>
			<Link to="/resource">
				<Button type="ghost" size="large">
					<Icon type="pie-chart" />
					<br/>
					教室查询
				</Button>
			</Link>
			<Link to="/reserve">
				<Button type="ghost" size="large">
					<Icon type="home" />
					<br/>
					教室申请
				</Button>
			</Link>
			<br />
			<Link to="/reserve">
				<Button type="ghost" size="large">
					<Icon type="solution" />
					<br/>
					咨询申请
				</Button>
			</Link>
			<Link to="/result">
				<Button type="ghost" size="large">
					<Icon type="file-unknown" />
					<br/>
					结果查询
				</Button>
			</Link>
		</div>;
	}
});

var RoomDetail = React.createClass({
	render: function() {
		return <div id="RoomDetail">
			<Row>
				<Col span="16">
					<img src="http://www.shanghaitech.edu.cn/upload/image/20150109/1007121922.jpg"></img>
				</Col>
				<Col span="8">
					<h1>炒鸡大活动室</h1><br />
					<span>位置：学生事务中心2楼203</span><br />
					<span>容纳人数：100 人</span><br />
					<span>负责人：习近平</span><br />
					<span>开放时间：工作日 6:00 ~ 18:00</span>
				</Col>
			</Row>
		</div>;
	}
});

var ResourceApp = React.createClass({
	getInitialState: function() {
		return {
			step: 0,
			resource_id: "",
			applicant_name: '',
			applicant_sid: '',
			applicant_phone: '',
			applicant_department: undefined,
			purpose: "",
			time_begin: undefined,
			duration: undefined,
			sn: undefined,
		};
	},
	render: function() {
		var eventHandler = {
			resource_id: function(event) {
				this.setState({resource_id: event.target.value})
			}.bind(this),
			applicant_name: function(event) {
				this.setState({applicant_name: event.target.value})
			}.bind(this),
			applicant_sid: function(event) {
				this.setState({applicant_sid: event.target.value})
			}.bind(this),
			applicant_phone: function(event) {
				this.setState({applicant_phone: event.target.value})
			}.bind(this),
			applicant_department: function(event) {
				this.setState({applicant_department: event})
			}.bind(this),
			purpose: function(event) {
				this.setState({purpose: event.target.value})
			}.bind(this),
			time_begin: function(event) {
				this.setState({time_begin: event.valueOf()})
			}.bind(this),
			duration: function(event) {
				this.setState({duration: event})
			}.bind(this),
			next: function(event) {
				this.setState({step: this.state.step + 1})
			}.bind(this),
			redo: function(event) {
				this.setState({step: this.state.step - 1})
			}.bind(this),
			submit: function(event) {
				this.props.eventHandler.setLoad();
				// TODO：SUBMIT
				this.setState({sn:"100100"})
				this.props.eventHandler.stopLoad();
			}.bind(this),
		};
		return <div id="ReserveApp">
			<ReserveSteps step={this.state.step} />
			<ReserveForm
				state={this.state}
				eventHandler={eventHandler} />
		</div>;
	}
});

var ReserveSteps = React.createClass({
	render: function() {
		return <div id="ReserveSteps">
			<Steps current={this.props.step}>
				<Step title="申请对象" icon="share-alt" />
				<Step title="申请资料" icon="solution" />
				<Step title="提交申请" icon="check" />
			</Steps>
		</div>;
	}
});

var ReserveFormStep0 = React.createClass({
	render: function() {
		return <div id="ReserveFormStep0">
			<input type="hidden" value="0" />
			<RoomDetail />
			<Button
				type="primary"
				id="ReserveFormNext"
				disabled={!this.props.state.resource_id}
				onClick={this.props.eventHandler.next}>
				下一步
				<Icon type="caret-right" />
			</Button>
		</div>;
	}
});

var ReserveFormStep1 = React.createClass({
	render: function() {
		return <div id="ReserveFormStep1">
			<FormItem
				hasFeedback={true}
				id="control-name"
				label="姓名："
				labelCol={{ span: 8 }}
				wrapperCol={{ span: 10 }}>
				<Input
					type="text"
					placeholder="请输入您的姓名"
					value={this.props.state.applicant_name}
					onChange={this.props.eventHandler.applicant_name} />
			</FormItem>
			<FormItem
				hasFeedback={true}
				id="control-phone"
				label="学号："
				labelCol={{ span: 8 }}
				wrapperCol={{ span: 10 }}>
				<Input
					type="text"
					placeholder="请输入您的学号"
					value={this.props.state.applicant_sid}
					onChange={this.props.eventHandler.applicant_sid} />
			</FormItem>
			<FormItem
				hasFeedback={true}
				id="control-phone"
				label="手机号码："
				labelCol={{ span: 8 }}
				wrapperCol={{ span: 10 }}>
				<Input
					type="text"
					placeholder="请输入您的手机号码"
					value={this.props.state.applicant_phone}
					onChange={this.props.eventHandler.applicant_phone} />
			</FormItem>
			<FormItem
				hasFeedback={true}
				id="control-department"
				label="学院："
				labelCol={{ span: 8 }}
				wrapperCol={{ span: 10 }}>
				<Select
					showSearch
					placeholder="请选择学院"
					optionFilterProp="children"
					notFoundContent="无法找到"
					searchPlaceholder="输入关键词"
					value={this.props.state.applicant_department}
					onChange={this.props.eventHandler.applicant_department}>
					<Option value="jack">杰克</Option>
					<Option value="lucy">露西</Option>
					<Option value="tom">汤姆</Option>
				</Select>
			</FormItem>
			<FormItem
				hasFeedback={true}
				id="control-purpose"
				label="使用目的："
				labelCol={{ span: 8 }}
				wrapperCol={{ span: 10 }}>
				<Input
					type="textarea"
					placeholder="请输入使用目的"
					rows="3"
					value={this.props.state.purpose}
					onChange={this.props.eventHandler.purpose} />
			</FormItem>
			<FormItem
				hasFeedback={true}
				id="control-purpose"
				label="预约时间："
				labelCol={{ span: 8 }}
				wrapperCol={{ span: 10 }}>
				<DatePicker
					style={{width:"48%"}}
					showTime="true"
					format="yyyy-MM-dd HH:mm:ss"
					value={this.props.state.time_begin ? new Date(this.props.state.time_begin) : undefined}
					onChange={this.props.eventHandler.time_begin} />
				<Select
					style={{width:"48%", marginLeft:"4%"}}
					placeholder="请选择持续时间"
					value={this.props.state.duration}
					onChange={this.props.eventHandler.duration}>
					<Option value="1">30分钟</Option>
					<Option value="2">60分钟</Option>
					<Option value="3">90分钟</Option>
					<Option value="4">120分钟</Option>
					<Option value="5">150分钟</Option>
				</Select>
			</FormItem>
			<Button
				type="primary"
				id="ReserveFormRedo"
				onClick={this.props.eventHandler.redo}>
				<Icon type="caret-left" />
				上一步
			</Button>
			<Button
				type="primary"
				id="ReserveFormNext"
				disabled={!(
					this.props.state.applicant_name &&
					this.props.state.applicant_sid &&
					this.props.state.applicant_phone &&
					this.props.state.applicant_department &&
					this.props.state.purpose &&
					this.props.state.time_begin &&
					this.props.state.duration
				)}
				onClick={this.props.eventHandler.submit}>
				提交申请
				<Icon type="caret-right" />
			</Button>
		</div>;
	}
});

var ReserveFormStep2 = React.createClass({
	render: function() {
		return <div id="ReserveFormStep2">
			<Icon type="smile" />
			<h1>申请完成</h1>
			<h3>请耐心等待审核</h3><br />
			<p>本次申请的查询代码：100110</p><br />
			<Link to="/">
				<Button type="primary">
					<Icon type="home" />
					返回
				</Button>
			</Link>
		</div>;
	}
});

var ReserveForm = React.createClass({
	render: function() {
		if (this.props.state.step == 0)
			var ReserveFormStep = ReserveFormStep0
		else if (this.props.state.step == 1)
			var ReserveFormStep = ReserveFormStep1
		else if (this.props.state.step == 2)
			var ReserveFormStep = ReserveFormStep2;

		return <Form horizontal className="form" >
			<ReserveFormStep
				state={this.props.state}
				eventHandler={this.props.eventHandler} />
		</Form>;
	}
});

var ReserveApp = React.createClass({
	getInitialState: function() {
		return {
			step: 0,
			resource_id: "",
			applicant_name: '',
			applicant_sid: '',
			applicant_phone: '',
			applicant_department: undefined,
			purpose: "",
			time_begin: undefined,
			duration: undefined,
			sn: undefined,
		};
	},
	render: function() {
		var eventHandler = {
			resource_id: function(event) {
				this.setState({resource_id: event.target.value})
			}.bind(this),
			applicant_name: function(event) {
				this.setState({applicant_name: event.target.value})
			}.bind(this),
			applicant_sid: function(event) {
				this.setState({applicant_sid: event.target.value})
			}.bind(this),
			applicant_phone: function(event) {
				this.setState({applicant_phone: event.target.value})
			}.bind(this),
			applicant_department: function(event) {
				this.setState({applicant_department: event})
			}.bind(this),
			purpose: function(event) {
				this.setState({purpose: event.target.value})
			}.bind(this),
			time_begin: function(event) {
				this.setState({time_begin: event.valueOf()})
			}.bind(this),
			duration: function(event) {
				this.setState({duration: event})
			}.bind(this),
			next: function(event) {
				this.setState({step: this.state.step + 1})
			}.bind(this),
			redo: function(event) {
				this.setState({step: this.state.step - 1})
			}.bind(this),
			submit: function(event) {
				this.props.eventHandler.setLoad();
				// TODO：SUBMIT
				this.setState({sn:"100100"})
				this.props.eventHandler.stopLoad();
			}.bind(this),
		};
		return <div id="ReserveApp">
			<ReserveSteps step={this.state.step} />
			<ReserveForm
				state={this.state}
				eventHandler={eventHandler} />
		</div>;
	}
});

var ReservationDetail = React.createClass({
	render: function() {
		return <div id="ReservationDetail">
			<RoomDetail />
			<Form horizontal className="form" >
				<Col span="12">
					<FormItem
						hasFeedback={true}
						id="control-name"
						label="姓名："
						labelCol={{ span: 10 }}
						wrapperCol={{ span: 8 }}>
						{this.props.data.applicant_name}
					</FormItem>
					<FormItem
						hasFeedback={true}
						id="control-phone"
						label="手机号码："
						labelCol={{ span: 10 }}
						wrapperCol={{ span: 8 }}>
						{this.props.data.applicant_phone}
					</FormItem>
					<FormItem
						hasFeedback={true}
						id="control-purpose"
						label="预约时间："
						labelCol={{ span: 10 }}
						wrapperCol={{ span: 8 }}>
						{this.props.data.time_begin}
						{this.props.data.time_end}
					</FormItem>
				</Col>
				<Col span="12">
					<FormItem
						hasFeedback={true}
						id="control-phone"
						label="学号："
						labelCol={{ span: 8 }}
						wrapperCol={{ span: 10 }}>
						{this.props.data.applicant_sid}
					</FormItem>
					<FormItem
						hasFeedback={true}
						id="control-department"
						label="学院："
						labelCol={{ span: 8 }}
						wrapperCol={{ span: 10 }}>
						<Select value={this.props.data.applicant_phone}>
							<Option value="jack">杰克</Option>
							<Option value="lucy">露西</Option>
							<Option value="tom">汤姆</Option>
						</Select>
					</FormItem>
					<FormItem
						hasFeedback={true}
						id="control-purpose"
						label="查询代码："
						labelCol={{ span: 8 }}
						wrapperCol={{ span: 10 }}>
						{this.props.data.sn}
					</FormItem>
				</Col>
				<FormItem
					hasFeedback={true}
					id="control-purpose"
					label="使用目的："
					labelCol={{ span: 5 }}
					wrapperCol={{ span: 12 }}>
					<pre>
						{this.props.data.purpose}
					</pre>
				</FormItem>
			</Form>
			<h1>申请状态：申请通过</h1>
		</div>;
	}
});

var ResultApp = React.createClass({
	getInitialState: function() {
		return {
			step: 0,
			data: undefined,
			sn: undefined,
		};
	},
	render: function() {
		var eventHandler = {
			sn: function(event) {
				this.setState({sn: event.target.value})
			}.bind(this),
			applicant_name: function(event) {
				this.setState({applicant_name: event.target.value})
			}.bind(this),
			applicant_sid: function(event) {
				this.setState({applicant_sid: event.target.value})
			}.bind(this),
			applicant_phone: function(event) {
				this.setState({applicant_phone: event.target.value})
			}.bind(this),
			applicant_department: function(event) {
				this.setState({applicant_department: event})
			}.bind(this),
			purpose: function(event) {
				this.setState({purpose: event.target.value})
			}.bind(this),
			time_begin: function(event) {
				this.setState({time_begin: event.valueOf()})
			}.bind(this),
			duration: function(event) {
				this.setState({duration: event})
			}.bind(this),
			next: function(event) {
				this.setState({step: this.state.step + 1})
			}.bind(this),
			redo: function(event) {
				this.setState({step: this.state.step - 1})
			}.bind(this),
			submit: function(event) {
				this.props.eventHandler.setLoad();
				// TODO：SUBMIT
				this.setState({data:{
					resource_id: 1,
					applicant_name: 'aaa',
					applicant_sid: '123123',
					applicant_phone: '1111111',
					applicant_department: "1",
					purpose: "啊实打实大\nasdasdas\n",
					time_begin: "123123123123",
					time_end: "123123123123",
					sn: 100100,
				}})
				this.setState({sn:"100100"})
				this.props.eventHandler.stopLoad();
			}.bind(this),
		};
		return <div id="ResultApp">
			<Icon type="smile" />
			<h1>结果查询</h1><br />
			<FormItem
				hasFeedback={true}
				id="control-phone"
				label="查询代码："
				labelCol={{ span: 9 }}
				wrapperCol={{ span: 8 }}>
				<Input
					style={{width:"68%"}}
					type="text"
					placeholder="请输入您的查询代码"
					size="small"
					value={this.state.sn}
					onChange={eventHandler.sn} />
				<Button
					style={{width:"28%", marginLeft:"4%"}}
					type="ghost"
					size="small"
					onClick={eventHandler.submit}>
					<Icon type="check" />
					查询
				</Button>
			</FormItem><br />
			{(this.state.data)
				? <ReservationDetail data={this.state.data} />
				: <br />
			}
			<br />
			<Link to="/">
				<Button type="primary">
					<Icon type="home" />
					返回
				</Button>
			</Link>
		</div>;
	}
});

var App = React.createClass({
	getInitialState: function() {
		return {
			loading: false,
		};
	},
	render: function() {
		var eventHandler = {
			setLoad: function(event) {
				this.setState({loading: true})
			}.bind(this),
			stopLoad: function(event) {
				this.setState({loading: false})
			}.bind(this),
		};

		if (this.props.route.path == "/")
			var ViewApp = IndexApp
		else if (this.props.route.path == "/resource")
			var ViewApp = ResourceApp
		else if (this.props.route.path == "/reserve")
			var ViewApp = ReserveApp
		else if (this.props.route.path == "/result")
			var ViewApp = ResultApp;

		return <div className="card">
			<Spin spining={this.state.loading}>
				<Breadcrumbs route={this.props.route} />
				<ViewApp eventHandler={eventHandler} />
			</Spin>
		</div>;
	}
});

var RouteApp = React.createClass({
	render: function() {
		return <Router history={hashHistory}>
			<Route path="/" component={App}/>
			<Route path="/resource" component={App}/>
			<Route path="/reserve" component={App}/>
			<Route path="/result" component={App}/>
		</Router>;
	}
});

export default RouteApp;
// export default IndexApp;
// export default ReserveApp;
// export default ResultApp;

