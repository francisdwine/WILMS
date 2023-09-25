-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 25, 2023 at 06:05 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `wallet_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_user'),
(22, 'Can change user', 6, 'change_user'),
(23, 'Can delete user', 6, 'delete_user'),
(24, 'Can view user', 6, 'view_user'),
(25, 'Can add user profile info', 7, 'add_userprofileinfo'),
(26, 'Can change user profile info', 7, 'change_userprofileinfo'),
(27, 'Can delete user profile info', 7, 'delete_userprofileinfo'),
(28, 'Can view user profile info', 7, 'view_userprofileinfo'),
(29, 'Can add transaction', 8, 'add_transaction'),
(30, 'Can change transaction', 8, 'change_transaction'),
(31, 'Can delete transaction', 8, 'delete_transaction'),
(32, 'Can view transaction', 8, 'view_transaction');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(8, 'wallet', 'transaction'),
(6, 'wallet', 'user'),
(7, 'wallet', 'userprofileinfo');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-09-14 03:00:21.453792'),
(2, 'contenttypes', '0002_remove_content_type_name', '2023-09-14 03:00:21.520605'),
(3, 'auth', '0001_initial', '2023-09-14 03:00:21.839666'),
(4, 'auth', '0002_alter_permission_name_max_length', '2023-09-14 03:00:21.907741'),
(5, 'auth', '0003_alter_user_email_max_length', '2023-09-14 03:00:21.919772'),
(6, 'auth', '0004_alter_user_username_opts', '2023-09-14 03:00:21.928410'),
(7, 'auth', '0005_alter_user_last_login_null', '2023-09-14 03:00:21.936161'),
(8, 'auth', '0006_require_contenttypes_0002', '2023-09-14 03:00:21.936161'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2023-09-14 03:00:21.952768'),
(10, 'auth', '0008_alter_user_username_max_length', '2023-09-14 03:00:21.963263'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2023-09-14 03:00:21.968562'),
(12, 'auth', '0010_alter_group_name_max_length', '2023-09-14 03:00:22.004007'),
(13, 'auth', '0011_update_proxy_permissions', '2023-09-14 03:00:22.014998'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2023-09-14 03:00:22.020729'),
(15, 'wallet', '0001_initial', '2023-09-14 03:00:22.649162'),
(16, 'admin', '0001_initial', '2023-09-14 03:00:22.841638'),
(17, 'admin', '0002_logentry_remove_auto_add', '2023-09-14 03:00:22.855893'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2023-09-14 03:00:22.859692'),
(19, 'sessions', '0001_initial', '2023-09-14 03:00:22.917985');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('114pyv2boz8jtk6gi7arlzadv3qfe2or', 'e30:1qkmtQ:v4uspFE_BeboPVKqSzhLdCDWX6YKIaZzloi_vYwuBCc', '2023-10-09 14:49:00.696553'),
('84wxbh6ikrqvll0cmhgr2uxuqj6um2zu', 'e30:1qkmnK:1rvpVytfoNashVHFGhr_uR_2lfFMNombhqzu9eq-N-0', '2023-10-09 14:42:42.114634'),
('bmrw9l2uyfd2abn1467ebibn7fhj8ps0', '.eJxVjDsOwjAQBe_iGll4_Yso6TmDtetdkwCypTipIu4OkVJA-2bmbSrhuoxp7TKnidVFgTr9boT5KXUH_MB6bzq3uswT6V3RB-361lhe18P9Oxixj9_aeQqDcPSGHDIhhCAIkDOIKVSisxYGQM9ELhZ7pihiZPBivDEspN4f_Uo4rA:1qhPhd:iVskYqKCo3-b1EO1fZYtFaj17XoorkyH-SvRvzm7Res', '2023-09-30 07:26:53.356668'),
('c2pl93yy953q0j74p5989h2b85jjwcm8', '.eJxVjDkOwjAUBe_iGlmO-V6gpOcMkf0XHEC2FCcV4u4QKQW0b2beS41pXcq4dp7HidRZHdXhd8sJH1w3QPdUb01jq8s8Zb0peqddXxvx87K7fwcl9fKtxWfBlGyIEQOAj0QcEIGI5CTs3MAsTjKBdcYDw-Awks02OAFjSL0_IYo5BA:1qknjj:NsV9KE2iPdWikH37BGOnGQrbTux9aRV7lpTCf-B6hBU', '2023-10-09 15:43:03.312787'),
('d15wf8250s8wo8jfc35ffyug9taxt0ds', 'e30:1qhPWt:gSmMPyXwWLCtNV5eWkD_8Lf0Q0pE6bat4JtgHY0R2Ys', '2023-09-30 07:15:47.916793'),
('icmozedkcwm5q00ta0o2y3oezsqrpua7', 'e30:1qhPgq:063lRf6DFiaJ11IDuWewwyk6U8oe20XWyDzIUyQ_YAc', '2023-09-30 07:26:04.535943'),
('ipx4qjdcck8gydosgro8bcu68n2tnfeu', 'e30:1qhPar:bonslTcv_ePLmD87nsG8mZOY-eWs4qffFO2qSKWsLlg', '2023-09-30 07:19:53.705727'),
('lwle7jkx27gm2ldvmthj2m9n8pamcs10', 'e30:1qiEBw:CaNbCM0N5_4socm96_n_yuEmNcnTdHh7mPT0F-owebk', '2023-10-02 13:21:32.568560'),
('mjjnq62bde1b33f3jbj0jo3ve3kobhhl', 'e30:1qhPdt:T_59zVSfpwIhUqbDKoi8IdmvmkC0Il4qCD8ZWAJHXdM', '2023-09-30 07:23:01.217091'),
('n8oxf3fuevvkqpkyahfkdzlrwmsqd5ne', 'e30:1qhPdC:9mqBj5MrDV9TPZtd1hRh7josp2v_i2jSQx8v2-nZdMw', '2023-09-30 07:22:18.423338'),
('oiez56inzcxwqlnwxs56vsl9r1unskpk', 'e30:1qiEAt:aKNFgLR9vX0CfgVLBF5v4u56RJsQ-DzuoPtzWC_yKEE', '2023-10-02 13:20:27.891847'),
('rkv29090k2ds1mbi45jiy2fyzjtu5ko6', 'e30:1qkmuF:ZxUzBgWqiklsLcOF0VVQXfFvGDUwge4cj71bhfE6nmg', '2023-10-09 14:49:51.828524'),
('udrav54wylca0gjoplyxh4bc5mm1nq3n', '.eJxVjDsOwjAQBe_iGll4_Yso6TmDtetdkwCypTipIu4OkVJA-2bmbSrhuoxp7TKnidVFgTr9boT5KXUH_MB6bzq3uswT6V3RB-361lhe18P9Oxixj9_aeQqDcPSGHDIhhCAIkDOIKVSisxYGQM9ELhZ7pihiZPBivDEspN4f_Uo4rA:1qiDyF:YxeSZLSRJeM2RYKy_tS3r1MAIX6WtvCwC-xGtsGjh6o', '2023-10-02 13:07:23.046670'),
('vkgobayru69pw0l5ohm70xhbcwndexny', 'e30:1qkmkk:optLvyjlNKEJtmEXCgclEWAWdgncFp14nGI9_LWVUzI', '2023-10-09 14:40:02.240846'),
('xb0kf895t03yqeo3xe4ytbj7asw07zt9', 'e30:1qhPgO:1K86cdK4WqssRsNLXG1p-emSje7Iv3U3jx-6fhDW7nM', '2023-09-30 07:25:36.473454');

-- --------------------------------------------------------

--
-- Table structure for table `wallet_transaction`
--

CREATE TABLE `wallet_transaction` (
  `transactionID` int(11) NOT NULL,
  `points` decimal(10,2) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `recipient_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `wallet_transaction`
--

INSERT INTO `wallet_transaction` (`transactionID`, `points`, `date`, `time`, `recipient_id`) VALUES
(1, 12.00, '2023-09-14', '11:22:36.312459', 1),
(2, 100.00, '2023-09-25', '23:31:49.409449', 2),
(3, 100.00, '2023-09-25', '23:43:11.568312', 3),
(4, 100.00, '2023-09-25', '23:55:44.177319', 3);

-- --------------------------------------------------------

--
-- Table structure for table `wallet_user`
--

CREATE TABLE `wallet_user` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `wallet_user`
--

INSERT INTO `wallet_user` (`id`, `password`, `last_login`, `is_superuser`, `email`, `is_staff`, `is_active`) VALUES
(1, 'pbkdf2_sha256$600000$iPioeqgtFfHXVGhzZfVP5T$Ym0lqYhydvW9LcUw5BPdk4P59Ti9jAaG+3/905IqYHQ=', '2023-09-14 03:38:10.588350', 0, 'kirk@gmail.com', 0, 1),
(2, 'pbkdf2_sha256$600000$QEgVsXa7ZfXCl1rt86YVyl$oXSpo330U9H4Sx6C5mZ8us6qCk+78PtCKt3SE6DzLWE=', '2023-09-25 15:31:33.829336', 0, '1234@gmail.com', 0, 1),
(3, 'pbkdf2_sha256$600000$yLDxvgNLskEfllcPOLKk5U$hoOtVajTscDKxuQA+EMht4+4f7unW9mH6IwWxa9Dqxw=', '2023-09-25 15:43:03.298080', 0, '12345@gmail.com', 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `wallet_userprofileinfo`
--

CREATE TABLE `wallet_userprofileinfo` (
  `profile_id` int(11) NOT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `coin_balance` double NOT NULL,
  `point_balance` double NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `wallet_userprofileinfo`
--

INSERT INTO `wallet_userprofileinfo` (`profile_id`, `first_name`, `last_name`, `coin_balance`, `point_balance`, `user_id`) VALUES
(1, 'kirk', '1234', 0, 12, 1),
(2, 'kirk', 'montejo', 0, 100, 2),
(3, 'tester1', 'Montejo', 1234, 200, 3);

-- --------------------------------------------------------

--
-- Table structure for table `wallet_user_groups`
--

CREATE TABLE `wallet_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `wallet_user_user_permissions`
--

CREATE TABLE `wallet_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_wallet_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `wallet_transaction`
--
ALTER TABLE `wallet_transaction`
  ADD PRIMARY KEY (`transactionID`),
  ADD KEY `wallet_transaction_recipient_id_1322686c_fk_wallet_user_id` (`recipient_id`);

--
-- Indexes for table `wallet_user`
--
ALTER TABLE `wallet_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `wallet_userprofileinfo`
--
ALTER TABLE `wallet_userprofileinfo`
  ADD PRIMARY KEY (`profile_id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `wallet_user_groups`
--
ALTER TABLE `wallet_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `wallet_user_groups_user_id_group_id_0f92998f_uniq` (`user_id`,`group_id`),
  ADD KEY `wallet_user_groups_group_id_afebb77c_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `wallet_user_user_permissions`
--
ALTER TABLE `wallet_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `wallet_user_user_permissions_user_id_permission_id_869eff45_uniq` (`user_id`,`permission_id`),
  ADD KEY `wallet_user_user_per_permission_id_d9f70bdc_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `wallet_transaction`
--
ALTER TABLE `wallet_transaction`
  MODIFY `transactionID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `wallet_user`
--
ALTER TABLE `wallet_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `wallet_userprofileinfo`
--
ALTER TABLE `wallet_userprofileinfo`
  MODIFY `profile_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `wallet_user_groups`
--
ALTER TABLE `wallet_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `wallet_user_user_permissions`
--
ALTER TABLE `wallet_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_wallet_user_id` FOREIGN KEY (`user_id`) REFERENCES `wallet_user` (`id`);

--
-- Constraints for table `wallet_transaction`
--
ALTER TABLE `wallet_transaction`
  ADD CONSTRAINT `wallet_transaction_recipient_id_1322686c_fk_wallet_user_id` FOREIGN KEY (`recipient_id`) REFERENCES `wallet_user` (`id`);

--
-- Constraints for table `wallet_userprofileinfo`
--
ALTER TABLE `wallet_userprofileinfo`
  ADD CONSTRAINT `wallet_userprofileinfo_user_id_191a87f0_fk_wallet_user_id` FOREIGN KEY (`user_id`) REFERENCES `wallet_user` (`id`);

--
-- Constraints for table `wallet_user_groups`
--
ALTER TABLE `wallet_user_groups`
  ADD CONSTRAINT `wallet_user_groups_group_id_afebb77c_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `wallet_user_groups_user_id_9eb02b0d_fk_wallet_user_id` FOREIGN KEY (`user_id`) REFERENCES `wallet_user` (`id`);

--
-- Constraints for table `wallet_user_user_permissions`
--
ALTER TABLE `wallet_user_user_permissions`
  ADD CONSTRAINT `wallet_user_user_per_permission_id_d9f70bdc_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `wallet_user_user_permissions_user_id_908340e2_fk_wallet_user_id` FOREIGN KEY (`user_id`) REFERENCES `wallet_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
