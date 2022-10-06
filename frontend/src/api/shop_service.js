import {api} from 'boot/axios'
import projectComposables from "src/api/composables"

export default class ShopService {
    async refreshToken() {
        const { access, refresh } = projectComposables()

        return new Promise((resolve, reject) => {
            api.post('/auth/token/refresh/', { refresh: refresh.value }).then((resp) => {
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

    async getCart(cartID) {
        return api.get(`/shop/cart/${cartID}/`)
    }

    async updateCart(cartID, cart_item, quantity) {
        return api.post(`/shop/cart/${cartID}/update/`, {cart_item: cart_item, qty: quantity})
    }

    async addItemToCart(cartID, itemID) {
        return api.post(`/shop/cart/${cartID}/add/`, {item: itemID})
    }


    async checkoutCart(country_code, cart_items) {
        return api.post(`/shop/cart/checkout/`, {country_code: country_code, cart_items: cart_items})
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
