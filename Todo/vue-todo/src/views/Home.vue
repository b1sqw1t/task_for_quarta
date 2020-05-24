<template>
    <div class="home">
        <table class="table table-dark">
            <thead>
            <tr>
                <td><h3>Описание дела</h3></td>
                <td><h3>Дата создания</h3></td>
                <td><h3>Дедлайн</h3></td>
                <td><h3>Статус задачи</h3></td>
                <td><h3>Дата выполнения</h3></td>
                <td>Управление</td>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(todo, index) in this.listTodo.length">
                <td v-if="listTodo[index].change"><input type="text" class="form-control"
                                                         v-model="listTodo[index].todo"></td>
                <td v-else>{{ listTodo[index].todo }}</td>


                <td v-if="listTodo[index].change">{{ localeDate( listTodo[index].created) }}</td>
                <td v-else>{{ localeDate( listTodo[index].created) }}</td>


                <td v-if="listTodo[index].change">
                    <datetime type="datetime"
                              v-model="listTodo[index].expiry_date"
                              input-class="form-control">
                    </datetime>
                </td>
                <td v-else>{{ localeDate( listTodo[index].expiry_date) }}</td>


                <td v-if="listTodo[index].change">
                    <select class="form-control" v-model="listTodo[index].status">
                        <option value="true">Выполнено</option>
                        <option value="false">Не выполнено</option>
                    </select>
                </td>
                <td v-else>{{ StatusReturn(listTodo[index].status) }}</td>


                <td v-if="listTodo[index].change">
                    <datetime type="datetime"
                              v-model="listTodo[index].completion_date"
                              input-class="form-control">
                    </datetime>
                </td>
                <td v-else>{{ localeDate(listTodo[index].completion_date) }}</td>


                <td v-if="listTodo[index].change">
                    <button class="btn btn-block btn-success" @click="SaveUpdateTodo(index)">Сохранить</button>
                </td>
                <td v-else>
                       <span @click="UpdateTodo(index)">
                           <svg class="bi bi-pencil-square text-warning" width="1em" height="1em" viewBox="0 0 16 16"
                                fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                              <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456l-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                              <path fill-rule="evenodd"
                                    d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
                            </svg>
                       </span>
                    <span @click="DestroyTodo(index)">
                            <svg class="bi bi-trash text-danger" width="1em" height="1em" viewBox="0 0 16 16"
                                 fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                              <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
                              <path fill-rule="evenodd"
                                    d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4L4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
                            </svg>
                        </span>
                </td>

            </tr>
            <tr>
                <td><input v-model="Todoobject.todo" type="text" class="form-control" required></td>
                <td></td>
                <td>
                    <datetime type="datetime" v-model="Todoobject.expiry_date" input-class="form-control"></datetime>
                </td>
                <td>
                    <select v-model="Todoobject.status" class="form-control">
                        <option value="true">Выполнено</option>
                        <option value="false">Не выполнено</option>
                    </select>
                </td>
                <td>
                    <datetime type="datetime" v-model="Todoobject.completion_date"
                              input-class="form-control"></datetime>
                </td>
                <td>
                    <button @click="CreateTodo()" class="btn btn-block btn-success">Создать задачу</button>
                </td>
            </tr>
            </tbody>
        </table>
    </div>
</template>
<style>
    span {
        margin-left: 15px;
        font-size: 22px;
    }
</style>
<script>
    import Vue from 'vue'
    import {Datetime} from 'vue-datetime'
    import 'vue-datetime/dist/vue-datetime.css'

    Vue.use(Datetime)
    export default {
        name: 'Home',
        data() {
            return {
                listTodo: [],
                Todoobject: {
                    todo: '',
                    expiry_date: '',
                    status: '',
                    completion_date: '',
                }
            }
        },
        components: {
            datetime: Datetime
        },
        created() {
            this.loadTodoList()
        },

        methods: {
            StatusReturn(status) {
                if (status) {
                    return 'Выполнено'
                } else {
                    return "Не выполнено"
                }
            },
            async SaveUpdateTodo(index) {
                await fetch(`${this.$store.getters.getBackendUrl}RUDView/`+this.listTodo[index].id+'/', {
                    method: "put",
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },

                    //make sure to serialize your JSON body
                    body: JSON.stringify({
                        id: index,
                        todo: this.listTodo[index].todo,
                        expiry_date: this.listTodo[index].expiry_date,
                        status: this.listTodo[index].status,
                        completion_date: this.listTodo[index].completion_date
                    })
                }).then((response) => {
                    this.listTodo[index].change = false
                    this.loadTodoList()
                });


            },
            async DestroyTodo(index) {
                await fetch(`${this.$store.getters.getBackendUrl}RUDView/`+this.listTodo[index].id+'/', {
                    method: "delete",
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    }
                }).then((response) => {
                    this.loadTodoList()
                })
            },
            UpdateTodo(index) {
                this.listTodo[index].change = true
            },
            async loadTodoList() {
                this.listTodo = await fetch(
                    `${this.$store.getters.getBackendUrl}`
                ).then(response => response.json())
                console.log(this.listTodo)
            },

            localeDate(date) {
                return (new Date(date)).toLocaleDateString()
            },
            async CreateTodo() {
                await fetch(`${this.$store.getters.getBackendUrl}`, {
                    method: "post",
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },

                    //make sure to serialize your JSON body
                    body: JSON.stringify({
                        todo: this.Todoobject.todo,
                        expiry_date: this.Todoobject.expiry_date,
                        status: this.Todoobject.status,
                        completion_date: this.Todoobject.completion_date
                    })
                }).then((response) => {
                    this.loadTodoList()
                });

            }
        }
    }
</script>
