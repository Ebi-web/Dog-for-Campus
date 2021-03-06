<?php require_once "./backend/doScraping.php";
echo "<div id='obtainedDom'>" . $dom . "</div>";
?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8" />
    <title>ToDo アプリ</title>
    <link rel="stylesheet" href="style.css" />
    <script src="https://unpkg.com/vue@3.0.0/dist/vue.global.js"></script>
</head>

<body>
    <h1>ToDo アプリ</h1>
    <div id="app">
        <div class="new-todo">
            <div class="new-todo-item">
                <label for="new-todo-title">タイトル</label>
                <input v-model.trim="todoTitle" type="text" id="new-todo-title" form="form-todo" />
            </div>
            <div class="new-todo-item">
                <label for="new-todo-description">説明</label>
                <textarea v-model.tirm="todoDescription" id="new-todo-description" form="form-todo"></textarea>
            </div>
            <div class="new-todo-category">
                カテゴリ
                <ul>
                    <li v-for="category in categories" :key="category">
                        <label :for="'category-' + category">
                            <input v-model="todoCategories" type="checkbox" :id="'category-' + category" :value="category" form="form-todo" />
                            {{ category }}
                        </label>
                    </li>
                </ul>
                <form @submit.prevent="createCategory">
                    <input v-model.trim="categoryName" type="text" />
                    <button type="submit" :disabled="!canCreateCategory">作成</button>
                </form>
            </div>
            <div class="new-todo-action">
                <form id="form-todo" @submit.prevent="createTodo">
                    <button type="submit" :disabled="!canCreateTodo">作成</button>
                </form>
            </div>
        </div>
        <div>
            <div class="todo-search">
                <div class="todo-search-item">
                    <label for="todo-search-category">カテゴリでフィルタ</label>
                    <select v-model="selectedCategory" id="todo-search-category">
                        <option value="">指定なし</option>
                        <option v-for="category in categories" :key="category" :value="category">
                            {{ category }}
                        </option>
                    </select>
                </div>
                <div class="todo-search-item">
                    <label for="todo-search-done">終了したものを非表示にする<input v-model="hideDoneTodo" type="checkbox" id="todo-search-done" /></label>
                </div>
                <div class="todo-search-item">
                    <select v-model="order">
                        <option value="desc">降順</option>
                        <option value="asc">昇順</option>
                    </select>
                </div>
                <div class="todo-search-item">
                    <label for="todo-search-keyword">キーワードで検索</label>
                    <input v-model.trim="searchWord" type="text" id="todo-search-keyword" />
                </div>
            </div>
            <ul v-if="hasTodos" class="todo-list">
                <li v-for="(todo, index) in resultTodos" :key="todo.id" class="todo-item">
                    <div class="todo-item-done">
                        <input v-model="todo.done" type="checkbox" />
                    </div>
                    <div class="todo-item-content">
                        <div class="todo-item-date">
                            {{ new Date(todo.dateTime).toString() }}
                        </div>
                        <h3 class="todo-item-title">{{ todo.title }}</h3>
                        <div v-if="todo.description" class="todo-item-description">
                            {{ todo.description }}
                        </div>
                        <ul class="todo-item-categories" v-if="todo.categories.length > 0">
                            <li v-for="category in todo.categories" :key="category" class="todo-item-category">
                                {{ category }}
                            </li>
                        </ul>
                    </div>
                </li>
            </ul>
            <p v-else>ToDoタスクはまだ登録されていません</p>
        </div>
    </div>
</body>

</html>

<script>
    Vue.createApp({
        data: function() {
            return {
                todoTitle: '',
                todoDescription: '',
                todoCategories: [],
                selectedCategory: '',
                todos: [],
                categories: [],
                hideDoneTodo: false,
                searchWord: '',
                order: 'desc',
                categoryName: '',
            }
        },
        computed: {
            canCreateTodo: function() {
                return this.todoTitle !== ''
            },
            canCreateCategory: function() {
                return this.categoryName !== '' && !this.existsCategory
            },
            existsCategory: function() {
                const categoryName = this.categoryName

                return this.categories.indexOf(categoryName) !== -1
            },
            hasTodos: function() {
                return this.todos.length > 0
            },
            resultTodos: function() {
                const selectedCategory = this.selectedCategory
                const hideDoneTodo = this.hideDoneTodo
                const order = this.order
                const searchWord = this.searchWord
                return this.todos
                    .filter(function(todo) {
                        return (
                            selectedCategory === '' ||
                            todo.categories.indexOf(selectedCategory) !== -1
                        )
                    })
                    .filter(function(todo) {
                        if (hideDoneTodo) {
                            return !todo.done
                        }
                        return true
                    })
                    .filter(function(todo) {
                        return (
                            todo.title.indexOf(searchWord) !== -1 ||
                            todo.description.indexOf(searchWord) !== -1
                        )
                    })
                    .sort(function(a, b) {
                        if (order === 'asc') {
                            return a.dateTime - b.dateTime
                        }
                        return b.dateTime - a.dateTime
                    })
            },
        },
        watch: {
            todos: {
                handler: function(next) {
                    window.localStorage.setItem('todos', JSON.stringify(next))
                },
                deep: true,
            },
            categories: {
                handler: function(next) {
                    window.localStorage.setItem('categories', JSON.stringify(next))
                },
                deep: true,
            },
        },
        methods: {
            createTodo: function() {
                if (!this.canCreateTodo) {
                    return
                }

                this.todos.push({
                    id: 'todo-' + Date.now(),
                    title: this.todoTitle,
                    description: this.todoDescription,
                    categories: this.todoCategories,
                    dateTime: Date.now(),
                    done: false,
                })

                this.todoTitle = ''
                this.todoDescription = ''
                this.todoCategories = []
            },
            createCategory: function() {
                if (!this.canCreateCategory) {
                    return
                }

                this.categories.push(this.categoryName)

                this.categoryName = ''
            },
        },
        created: function() {
            const todos = window.localStorage.getItem('todos')
            const categories = window.localStorage.getItem('categories')

            if (todos) {
                this.todos = JSON.parse(todos)
            }

            if (categories) {
                this.categories = JSON.parse(categories)
            }
        },
    }).mount('#app')
</script>
</body>

</html>