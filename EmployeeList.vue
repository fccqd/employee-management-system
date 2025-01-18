<template>
  <div>
    <h1>员工列表</h1>
    <ul>
      <li v-for="employee in employees" :key="employee.id">
        {{ employee.name }} - {{ employee.position }}
      </li>
    </ul>
    <form @submit.prevent="addEmployee">
      <input v-model="newEmployee.name" placeholder="Name" required>
      <input v-model="newEmployee.age" type="number" placeholder="Age" required>
      <input v-model="newEmployee.gender" placeholder="Gender" required>
      <input v-model="newEmployee.department_id" type="number" placeholder="Department ID" required>
      <input v-model="newEmployee.position" placeholder="Position" required>
      <button type="submit">Add Employee</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      employees: [],
      newEmployee: {
        name: '',
        age: null,
        gender: '',
        department_id: null,
        position: ''
      }
    };
  },
  created() {
    this.fetchEmployees();
  },
  methods: {
    fetchEmployees() {
      axios.get('http://localhost:5000/employees')
        .then(response => {
          console.log('Fetched Employees:', response.data); // 将获取的数据赋值给 employees 数组
          this.employees = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    addEmployee() {
      axios.post('http://localhost:5000/employees', this.newEmployee)
        .then(() => {
          this.fetchEmployees();
          this.newEmployee = {
            name: '',
            age: null,
            gender: '',
            department_id: null,
            position: ''
          };
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
}
</script>

