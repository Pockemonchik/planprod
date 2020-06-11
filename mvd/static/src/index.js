import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import 'antd/dist/antd.css';
import { Layout, Menu, Breadcrumb } from 'antd';
import { Tabs, Button, Table, Input, InputNumber, Popconfirm, Form } from 'antd';
import { NotificationOutlined, PieChartOutlined, FileOutlined  } from '@ant-design/icons';
import mvd from '../admin1/images/logo.png';

const { SubMenu } = Menu;
const { Header, Content, Footer, Sider } = Layout;
const { TabPane } = Tabs;

const columns2 = [
    {
        dataIndex: 'name',
    },
    {
        dataIndex: 'data',
        align: 'center'
    }
]

const data2 = [
    {
        key: '1',
        name: 'Сумма рейтинговых баллов',
        data: '145,05',
    }
]

const columns1 = [
    {
        dataIndex: 'name',
    },
    {
        dataIndex: 'data',
        align: 'center',
    },
  ];
  
  const data1 = [
    {
      key: '1',
      name: 'Учебная работа',
      data: '123,05'
    },
    {
      key: '2',
      name: 'Организационно-методическая работа',
      data: '123,05' 
    },
    {
      key: '3',
      name: 'Подготовка учебно-методических материалов',
      data: '123,05'
    },
    {
      key: '4',
      name: 'Педагогический контроль',
      data: '123,05'
    },
  ];

  const originData = [
    {
        key: '1',
        name: 'Общий объем учебной нагрузки',
        value: '850',
        points: '5',
    },
    {
        key: '2',
        name: 'Соотношение учебной аудиторной нагрузки к общей учебной нагрзкик к общей учебной нагрузке более 70%',
        value: '75%',
        points: '5',
    },
    {
        key: '3',
        name: 'Проведение занятий с сотрудниками практических подразделений',
        value: '150',
        points: '5',
    },
  ];


  const EditableCell = ({
    editing,
    dataIndex,
    title,
    inputType,
    record,
    index,
    children,
    ...restProps
  }) => {
    const inputNode = inputType === 'number' ? <InputNumber /> : <Input />;
    return (
      <td {...restProps}>
        {editing ? (
          <Form.Item
            name={dataIndex}
            style={{
              margin: 0,
            }}
            rules={[
              {
                required: true,
                message: `Please Input ${title}!`,
              },
            ]}
          >
            {inputNode}
          </Form.Item>
        ) : (
          children
        )}
      </td>
    );
  };
  
  const EditableTable = () => {
    const [form] = Form.useForm();
    const [data, setData] = useState(originData);
    const [editingKey, setEditingKey] = useState('');
  
    const isEditing = record => record.key === editingKey;
  
    const edit = record => {
      form.setFieldsValue({
        name: '',
        value: '',
        points: '',
        ...record,
      });
      setEditingKey(record.key);
    };
  
    const cancel = () => {
      setEditingKey('');
    };
  
    const save = async key => {
      try {
        const row = await form.validateFields();
        const newData = [...data];
        const index = newData.findIndex(item => key === item.key);
  
        if (index > -1) {
          const item = newData[index];
          newData.splice(index, 1, { ...item, ...row });
          setData(newData);
          setEditingKey('');
        } else {
          newData.push(row);
          setData(newData);
          setEditingKey('');
        }
      } catch (errInfo) {
        console.log('Validate Failed:', errInfo);
      }
    };
  
    const columns2 = [
      {
        title: 'Показатель',
        dataIndex: 'name',
        width: '25%',
        editable: false,
      },
      {
        title: 'Значение',
        dataIndex: 'value',
        width: '15%',
        editable: true,
      },
      {
        title: 'Баллы',
        dataIndex: 'points',
        width: '40%',
        editable: false,
      },
      {
        title: 'Ввод',
        dataIndex: 'operation',
        render: (_, record) => {
          const editable = isEditing(record);
          return editable ? (
            <span>
              <a
                href="javascript:;"
                onClick={() => save(record.key)}
                style={{
                  marginRight: 8,
                }}
              >
                Сохранить
              </a>
              <Popconfirm title="Sure to cancel?" onConfirm={cancel}>
                <a>Отмена</a>
              </Popconfirm>
            </span>
          ) : (
            <a disabled={editingKey !== ''} onClick={() => edit(record)}>
              Изменить
            </a>
          );
        },
      },
    ];
    const mergedColumns = columns2.map(col => {
      if (!col.editable) {
        return col;
      }
  
      return {
        ...col,
        onCell: record => ({
          record,
        //   inputType: col.dataIndex === 'value' ? 'number' : 'text',
          dataIndex: col.dataIndex,
          title: col.title,
          editing: isEditing(record),
        }),
      };
    });
    return (
      <Form form={form} component={false}>
        <Table
          components={{
            body: {
              cell: EditableCell,
            },
          }}
          bordered
          dataSource={data}
          columns={mergedColumns}
          rowClassName="editable-row"
          pagination={{
            onChange: cancel,
          }}
        />
      </Form>
    );
  };

ReactDOM.render(
    <Layout className="lay-out">
    <Header className="header">
      <div className="logo">
        <img src={mvd}></img>
      </div>
    </Header>
    <Content style={{ padding: '0 50px' }}>
      <Breadcrumb style={{ margin: '16px 0' }}>
        <Breadcrumb.Item>Главная</Breadcrumb.Item>
        <Breadcrumb.Item>Ретинговая оценка</Breadcrumb.Item>
      </Breadcrumb>
      <Layout className="site-layout-background" style={{ padding: '24px 0' }}>
        <Sider className="site-layout-background" width={300}>
          <Menu
            mode="inline"
            defaultSelectedKeys={['1']}
            defaultOpenKeys={['sub1']}
            style={{ height: '100%' }}
          >
            <Menu.Item key="6" icon={<PieChartOutlined />}>
              Подготовить документ
            </Menu.Item>
            <Menu.Item key="7" icon={<FileOutlined />}>
              Иные кнопки управления
            </Menu.Item>
            <Menu.Item key="8">
              ...
            </Menu.Item>
          </Menu>
        </Sider>
        <Content style={{ padding: '0 24px', minHeight: 280 }} className="content-block">
            <Tabs>
                <TabPane tab="Суммарные показатели реутинговой оценки" key="1">
                    <Table
                        columns={columns1}
                        dataSource={data1}
                        bordered
                        className="table-half"
                    />
                    <Table
                        columns={columns2}
                        dataSource={data2}
                        bordered
                        className="table-half"
                    />
                </TabPane>
                <TabPane tab="Учебная работа" key="2">
                    <EditableTable />
                </TabPane>
                <TabPane tab="Организационно-методическая работа" key="3">
                    <EditableTable />
                </TabPane>
                <TabPane tab="Подготовка учебно-методических материалов" key="4">
                    <EditableTable />
                </TabPane>
                <TabPane tab="Педагогический контроль" key="5">
                    <EditableTable />
                </TabPane>
            </Tabs> 
        </Content>
      </Layout>
    </Content>
  </Layout>,
document.getElementById("root")
)