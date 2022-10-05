import {api} from 'boot/axios'
import projectComposables from "src/api/composables"

export default class ShopService {
    async refreshToken() {
        const { access, refresh } = projectComposables()

        return new Promise((resolve, reject) => {
            api.post('/token/refresh/', { refresh: refresh.value }).then((resp) => {
                if (resp.data) {
                    access.value = resp.data.access
                    resolve(true)
                }
            })
        })

    }

    async login(username, password) {
        const { access, refresh } = projectComposables()

        return new Promise((resolve, reject) => {
            api.post('/auth/token/', { username: username, password: password }).then((resp) => {
                if (resp.status == 200) {
                    access.value = resp.data.access
                    refresh.value = resp.data.refresh
                    resolve(true)
                }
                else {
                    reject("Login failed")
                }
            })
        })
    }

    async getItemList() {
        return api.get('/shop/items/')
    }

    async getCart() {
        return api.get('/shop/cart/')
    }

    async updateCart(item_id, quantity) {
        console.log('updateCart', item_id, quantity)
        return api.post('/shop/cart/update/', {item: item_id, qty: quantity})
    }

    async logout() {
        return new Promise((resolve, reject) => {
            const { access, refresh } = projectComposables()
            access.value = null
            refresh.value = null
            resolve(true)
        })
    }
}
