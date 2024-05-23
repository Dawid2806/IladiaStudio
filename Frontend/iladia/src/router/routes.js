const routes = [
  {
    path: "/",
    component: () => import("layouts/LoginLayout.vue"),
    children: [{ path: "", component: () => import("pages/IndexPage.vue") }],
  },
  {
    path: "/tatto",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: "",
        component: () => import("pages/Tatto/DashboardPage.vue"),
      },
      {
        path: "/tatto/clients",
        component: () => import("pages/Tatto/ClientsPage.vue"),
      },
      {
        path: "/tatto/clients/add-new",
        component: () => import("pages/Tatto/Clients/NewClientPage.vue"),
      },
      {
        path: "/tatto/clients/edit-:id",
        component: () => import("pages/Tatto/Clients/EditClientPage.vue"),
      },
      {
        path: "/tatto/client/:id",
        props: true,
        component: () => import("pages/Tatto/Clients/ClientPage.vue"),
      },
    ],
  },
  {
    path: "/nails",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: "",
        component: () => import("pages/Nails/DashboardPage.vue"),
      },
      {
        path: "/nails/clients",
        component: () => import("pages/Nails/ClientsPage.vue"),
      },
      {
        path: "/nails/clients/add-new",
        component: () => import("pages/Nails/Clients/NewClientPage.vue"),
      },
      {
        path: "/nails/clients/edit-:id",
        props: true,
        component: () => import("pages/Nails/Clients/EditClientPage.vue"),
      },
      {
        path: "/nails/client/:id",
        props: true,
        component: () => import("pages/Nails/Clients/ClientPage.vue"),
      },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
