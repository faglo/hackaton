<template>
  <v-row justify="center">
    <v-expansion-panels>
      <v-expansion-panel>
        <v-expansion-panel-header color="#EDF0F4"
          >Информация о клиенте</v-expansion-panel-header
        >
        <v-expansion-panel-content>
          <v-list>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-subtitle>ФИО</v-list-item-subtitle>
                <v-list-item-title
                  >Жмышенко Валерий Альбертович</v-list-item-title
                >
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-subtitle>Номер телефона</v-list-item-subtitle>
                <v-list-item-title>+7 (800) 555 35-35</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-subtitle>Социальные сети</v-list-item-subtitle>
                <v-list-item-title>vk.com/id59873294</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-subtitle
                  >Дополнительная информация</v-list-item-subtitle
                >
                <v-list-item-title
                  >Любая доп инфа про клиента</v-list-item-title
                >
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-expansion-panel-content>
      </v-expansion-panel>
      <v-expansion-panel>
        <v-expansion-panel-header color="#EDF0F4"
          >Информация о подборе объектов</v-expansion-panel-header
        >
        <v-expansion-panel-content>
          <v-list>
            <v-list-item style="margin-bottom: 8px" v-for="i in 4" :key="i">
              <v-card id="cont">
                <p
                  style="
                    display: flex;
                    justify-content: space-between;
                    font-size: 1rem;
                  "
                >
                  Сделка #6 <span>21.06.22</span>
                </p>
                <p>Двухкомнатная квартира в центре</p>
                <p>8 200 450 ₽</p>
              </v-card>
            </v-list-item>
          </v-list>
        </v-expansion-panel-content>
      </v-expansion-panel>
      <v-expansion-panel>
        <v-expansion-panel-header color="#EDF0F4"
          >История сделки</v-expansion-panel-header
        >
        <v-expansion-panel-content>
          <v-list>
            <v-list-item>
              <div>
                <div style="font-size: 0.8rem;color: #787878;margin-bottom: 6px; display: grid; grid-template-columns: 57px 1fr; gap: 16px">
                  <span style="text-align: right">Дата</span>
                  <span>Событие</span>
                </div>
                <div style="display:flex; gap: 16px" v-for="i in 3" :key="i">
                    <p>19.29.12</p>
                    <p>Обращение к агенту</p>
                </div>
              </div>
            </v-list-item>
          </v-list>
        </v-expansion-panel-content>
      </v-expansion-panel>
      <v-expansion-panel>
        <v-expansion-panel-header color="#EDF0F4"
          >Информация о клиенте</v-expansion-panel-header
        >
        <v-expansion-panel-content>
          <v-list>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-subtitle>ФИО</v-list-item-subtitle>
                <v-list-item-title
                  >Жмышенко Валерий Альбертович</v-list-item-title
                >
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-subtitle>Номер телефона</v-list-item-subtitle>
                <v-list-item-title>+7 (800) 555 35-35</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-subtitle>Социальные сети</v-list-item-subtitle>
                <v-list-item-title>vk.com/id59873294</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-subtitle
                  >Дополнительная информация</v-list-item-subtitle
                >
                <v-list-item-title
                  >Любая доп инфа про клиента</v-list-item-title
                >
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </v-row>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
#cont {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 4px 8px;
}
</style>