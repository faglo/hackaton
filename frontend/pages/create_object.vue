<template >
  <div>
    <v-expansion-panels accordion>
      <v-expansion-panel>
        <v-expansion-panel-header> Основные данные </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-card elevation="0" id="card">
            <v-card-title id="title"> Название объекта </v-card-title>
            <v-card-text>
              <v-text-field
                dense
                outlined
                placeholder="Введите название объекта"
              />
            </v-card-text>
          </v-card>
          <v-card elevation="0" id="card">
            <v-card-title id="title"> Выберите категорию объекта </v-card-title>
            <v-card-text>
              <v-text-field dense outlined placeholder="Категория объекта" />
            </v-card-text>
          </v-card>
          <v-card elevation="0" id="card">
            <v-card-title id="title"> Выберите тип объекта </v-card-title>
            <v-card-text>
              <v-text-field dense outlined placeholder="Тип объекта" />
            </v-card-text>
          </v-card>
          <v-card elevation="0" id="card">
            <v-card-title id="title"> Выберите тип реализации </v-card-title>
            <v-card-text>
              <v-text-field dense outlined placeholder="Тип реализации" />
            </v-card-text>
          </v-card>
          <v-card elevation="0" id="card">
            <v-card-title id="title"> Стоимость объекта </v-card-title>
            <v-card-text>
              <v-text-field
                dense
                outlined
                placeholder="Введите стоимость объекта"
              />
            </v-card-text>
          </v-card>
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header> Фотографии </v-expansion-panel-header>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header> Расположение </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-card elevation="0" id="card">
            <v-card-title id="title"> Город </v-card-title>
            <v-card-text>
              <v-text-field dense outlined placeholder="Введите город" />
            </v-card-text>
          </v-card>
          <v-card elevation="0" id="card">
            <v-card-title id="title"> Адрес </v-card-title>
            <v-card-text>
              <v-text-field dense outlined placeholder="Введите адрес" />
            </v-card-text>
          </v-card>
          <v-card elevation="0" id="card">
            <v-card-title id="title"> Жилой комплекс </v-card-title>
            <v-card-text>
              <v-text-field
                dense
                outlined
                placeholder="Введите жилой комплекс"
              />
            </v-card-text>
          </v-card>
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header> Характеристики </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-card elevation="0" id="card">
            <v-card-title id="title"> Описание (на сайте) </v-card-title>
            <v-card-text>
              <v-text-field dense outlined placeholder="Введите описание" />
            </v-card-text>
          </v-card>
          <v-card elevation="0" id="card">
            <v-card-title id="title"> Описание (внутреннее) </v-card-title>
            <v-card-text>
              <v-text-field dense outlined placeholder="Введите описание" />
            </v-card-text>
          </v-card>
          <v-card elevation="0" id="card">
            <v-card-title id="title"> Жилой комплекс </v-card-title>
            <v-card-text>
              <v-text-field
                dense
                outlined
                placeholder="Введите жилой комплекс"
              />
            </v-card-text>
          </v-card>
          <v-card elevation="0" id="card">
            <v-card-title id="title"> Жилая площадь </v-card-title>
            <v-card-text>
              <v-text-field dense outlined placeholder="Введите площадь" />
            </v-card-text>
          </v-card>
          <v-card elevation="0" id="card">
            <v-card-title id="title"> Площадь кухни </v-card-title>
            <v-card-text>
              <v-text-field dense outlined placeholder="Введите площадь" />
            </v-card-text>
          </v-card>
          <v-card elevation="0" id="card">
            <v-card-title id="title"> Количество комнат </v-card-title>
            <v-card-text>
              <v-text-field
                dense
                outlined
                placeholder="Введите количество комнат"
              />
            </v-card-text>
          </v-card>
          <v-card elevation="0" id="card">
            <v-card-title id="title"> Этаж </v-card-title>
            <v-card-text>
              <v-text-field dense outlined placeholder="Введите этаж" />
            </v-card-text>
          </v-card>
          <v-card elevation="0" id="card">
            <v-card-title id="title"> Этажность </v-card-title>
            <v-card-text>
              <v-text-field
                dense
                outlined
                placeholder="Введите количество этажей в доме"
              />
            </v-card-text>
          </v-card>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>

    <v-btn id="btn" x-large> Добавить объект </v-btn>
  </div>
</template>

<style lang="scss" scoped>
#title {
  font-size: 0.9rem;
  font-weight: normal;
  margin-bottom: -1rem;
  margin-top: -1rem;
}

#card {
  margin-bottom: -1rem;
}

#btn {
  margin-top: 1rem;
}
</style>
